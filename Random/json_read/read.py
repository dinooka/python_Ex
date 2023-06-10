import json

class FileRead:
    def read_json(self):
        with open('config.json',"r") as json_file:
            data = json.load(json_file)
            url = data['url']
            username = data['username']
            password = data['password']
        print(f"url={url}")
        print(f"username={username}")
        print(f"password={password}")

file = FileRead()
file.read_json()

