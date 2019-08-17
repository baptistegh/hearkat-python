import requests
import json

class Client:
    def __init__(self, userToken, accessToken):
        self.baseUrl = "https://api.hearkat.com"
        self.userToken = userToken
        self.accessToken = accessToken

    # PUSH a message on a specified channel
    def push(self, channel, message):
        headers = {
            "Content-Type": "application/json",
            "UserToken": self.userToken,
            "AccessToken": self.accessToken
        }
        req = requests.post(
            "{0}/channel/{1}".format(self.baseUrl, channel),
            headers=headers,
            data=message.to_json()
        )
        return req.status_code == 200

    # PULL on a specified channel
    def pull(self, channel):
        headers = {
            "Content-Type": "application/json",
            "UserToken": self.userToken,
            "AccessToken": self.accessToken
        }
        req = requests.get(
            "{0}/channel/{1}".format(self.baseUrl, channel),
            headers=headers
        )
        return { "status": req.status_code, "data" : json.loads(req.text) if req.status_code == 200 else None }

    # PULL on every channel
    def pullAll(self):
        headers = {
            "Content-Type": "application/json",
            "UserToken": self.userToken,
            "AccessToken": self.accessToken
        }
        req = requests.get(
            "{0}/channel".format(self.baseUrl),
            headers=headers
        )
        return { "status": req.status_code, "data" : json.loads(req.text) if req.status_code == 200 else None }
