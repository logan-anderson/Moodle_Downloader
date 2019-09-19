import requests
import re
from bs4 import BeautifulSoup
import json

def get_sesh_id(session):
    soup = BeautifulSoup(session.get('https://moodle31.upei.ca/login/index.php').text,"html.parser")
    return soup.find('input', attrs={'name':'logintoken'})['value']
    
config = json.loads(open('config.json', 'r').read())

session = requests.Session()
payload = {
    'logintoken': get_sesh_id(session),
    'username': config["username"],
    'password': config["password"]
}
session.post('https://moodle31.upei.ca/login/index.php', data=payload)

website = session.get("https://moodle31.upei.ca/course/view.php?id=" + config["course_id"])
html = website.text
# print(html)
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll(class_='activityinstance')

print('Downloaded:')
print('===========')
for name in config["downloaded"]:
    print(name)
print('================================================================================')
print('Downloading:')
print('===========')

for link in links:
    text = str(link)
    if config["match"] in text:
        quickSoup = BeautifulSoup(text, "html.parser")
        reference = quickSoup.find(class_="instancename").getText().replace(' File', '')
        if reference not in config["downloaded"]:
            url = quickSoup.find("a")['href']
            doc = session.get(url)
            disp = doc.headers.get('Content-disposition') 
            name = re.findall("filename.+", disp)[0].split("\"")[1]
            print(name)
            pdf = open( name, 'wb')
            pdf.write(doc.content)
            # log.write(reference)		
            config["downloaded"].append(reference)
config_file = open('config.json', 'w')
config_file.write(json.dumps(config))
config_file.close()
