import requests
import re
from bs4 import BeautifulSoup

def get_sesh_id(session):
    soup = BeautifulSoup(session.get('https://moodle31.upei.ca/login/index.php').text,"html.parser")
    return soup.find('input', attrs={'name':'logintoken'})['value']
    

#############################################################
match = "ecture"
course_id = "6378"
username = "acairns2"
password = 
#############################################################

session = requests.Session()



payload = {
    'logintoken': get_sesh_id(session),
    'username': username,
    'password': password
}
session.post('https://moodle31.upei.ca/login/index.php', data=payload)

website = session.get("https://moodle31.upei.ca/course/view.php?id=" + course_id)
html = website.text
# print(html)
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll(class_='activityinstance')

logged = open("Downloader.log", 'r')
downloaded = logged.read()
log = open("Downloader.log", 'a')
print(downloaded)
for link in links:
    text = str(link)
    if match in text:
        quickSoup = BeautifulSoup(text, "html.parser")
        reference = quickSoup.find(class_="instancename").getText().replace(' File', '')
        if reference not in downloaded:
            url = quickSoup.find("a")['href']
            doc = session.get(url)
            disp = doc.headers.get('Content-disposition') 
            name = re.findall("filename.+", disp)[0].split("\"")[1]
            print(name)
            pdf = open( name, 'wb')
            pdf.write(doc.content)
            log.write(reference)		


