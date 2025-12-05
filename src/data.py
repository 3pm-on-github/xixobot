import json

class Data:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "r") as f:
            self.data = json.load(f)
    
    def getMusicToken(self):
        return self.data.get("musicregtoken")
    
    def getToken(self):
        return self.data.get("token")
    
    def getXixoBankSignature(self):
        return self.data.get("xixobanksig")
    
    def getData(self):
        return (
            self.data.get("messages"),
            self.data.get("messagesuserid"),
            self.data.get("words"),
            self.data.get("wordsuserid"),
            self.data.get("msgcount"),
        )
    
    def saveData(self, messages, messagesuserid, words, wordsuserid, msgcount):
        self.data["messages"] = messages
        self.data["messagesuserid"] = messagesuserid
        self.data["words"] = words
        self.data["wordsuserid"] = wordsuserid
        self.data["msgcount"] = msgcount

        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)
