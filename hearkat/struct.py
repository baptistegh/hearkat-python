import json

class ShopItem:

    def __init__(self, title = None, price = None, link=None, image=None, merchant=None):
        #TODO: Add verifications
        self.title = title
        self.price = price
        self.link = link
        self.image = image
        self.merchant = merchant

    def __dict__(self):
        return {
            "title": self.title,
            "price": self.price,
            "link": self.link,
            "image": self.image,
            "merchant": self.merchant
        }

    def __eq__(self, other):
        return ( self.title == other.title and 
            self.price == other.price and 
            self.link == other.link and
            self.image == other.image and
            self.merchant == other.merchant)

class Notification: 
    def __init__(self, title = None, message = None, link=None, image=None):
        #TODO: Add verifications
        self.title = title
        self.message = message 
        self.link = link
        self.image = image

    def __dict__(self):
        return {
            "title": self.title,
            "message": self.message,
            "link": self.link,
            "image": self.image
        }

    def __eq__(self, other):
        return ( self.title == other.title and 
            self.message == other.message and 
            self.link == other.link and
            self.image == other.image )

class Message:
    notification = Notification()
    news = []
    chat = {}
    job = {}
    shopItem = ShopItem()
    event = {}
    metadata = {}
    tags = []

    def to_json(self):
        return_json = {}
        if self.notification != Notification():
            return_json['notification'] = self.notification.__dict__()
        if self.news != []:
            return_json['news'] = self.news
        if self.chat != {}:
            return_json['chat'] = self.chat
        if self.job != {}:
            return_json['job'] =self.job
        if self.shopItem != ShopItem():
            return_json['shopItem'] = self.shopItem.__dict__()
        if self.event != {}:
            return_json['event'] = self.event
        if self.metadata != {}:
            return_json['metadata'] = self.metadata
        if self.tags != []:
            return_json['tags'] = self.tags
        
        return json.dumps(return_json)