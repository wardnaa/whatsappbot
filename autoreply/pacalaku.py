import requests
import json
# simsimi bot 
class pacarku(object):

    def __init__(self, api, msg):
        self.api = api
        self.msg = msg

    def chatan(self):

        url = "https://wsapi.simsimi.com/190410/talk/"

        headers = {
            'Content-Type': "application/json",
            'x-api-key': self.api
        }

        datas = {
            "utext": self.msg,
            "lang": "id"
        }
        hook = requests.post(url, headers=headers, data=json.dumps(datas))
        pesan = json.loads(hook.text)
        value = pesan['atext']
        return value
