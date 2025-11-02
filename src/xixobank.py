import json

class XixoBank:
    def __init__(self, xixobankfile, signature):
        self.xixobankf = open(xixobankfile, "r+")
        self.xixobankdata = json.load(self.xixobankf)
        if self.xixobankdata["signature"] != signature:
            raise ValueError("Invalid Signature in xixobank file")

    def checkBalance(self, userid):
        if str(userid) in self.xixobankdata["balances"]:
            return self.xixobankdata["balances"][str(userid)]
        else:
            return "oopsie woopsie! looks like you don't have an account on the xixobank!"