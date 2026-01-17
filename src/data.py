import json

class Data:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("error: data file not found! make sure it exists in assets/data/data.json.")
            exit(1)

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
    
    def getAnomalocarisInfo(self):
        return (
            self.data.get("anomalocaris_name"),
            self.data.get("anomalocaris_dateofcreation"),
        )

    def saveAnomalocarisInfo(self, name):
        self.data["anomalocaris_name"] = name
        try:
            with open(self.filename, "w") as f:
                json.dump(self.data, f, indent=4)
            print(f"Successfully saved anomalocaris name: {name}")
        except Exception as e:
            print(f"Error saving anomalocaris data: {e}")
    
    def saveData(self, messages, messagesuserid, words, wordsuserid, msgcount):
        self.data["messages"] = messages
        self.data["messagesuserid"] = messagesuserid
        self.data["words"] = words
        self.data["wordsuserid"] = wordsuserid
        self.data["msgcount"] = msgcount

        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)
