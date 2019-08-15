import requests
import json

class Client:
    
    def __init__(self, userToken, accessToken):
        self.baseUrl = "https://api.hearkat.com"
        self.userToken = userToken
        self.accessToken = accessToken

    def push(self, channel, message):
        headers = {
            "Content-Type": "application/json",
            "UserToken": self.userToken,
            "AccessToken": self.accessToken
        }
        req = requests.post(
            "{0}/channel/{1}".format(self.baseUrl, channel),
            headers=headers,
            data=json.dumps(message)
        )
        return req.status_code == 200