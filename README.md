# Moodle Downloader
Use this to download notes from moodle.

## Usage
Rename config-template.json to config.json.
Fill in the required data in the file.

- match
    - What to match to link names. This is not case sensitive
- course_id
    - The number at the end of the url for a moodle course
- username and password
    - Your login credentials

Example config.json
```
{
     "match": "lecture",
     "downloaded": [],
     "course_id": "1234",
     "username": "jsmith",
     "password": "mygreatpassword"
}
```