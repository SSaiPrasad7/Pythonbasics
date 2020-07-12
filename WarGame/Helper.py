import json

class Helper:
    def readConfig(self,filename):
        with open(filename) as f:
            data=json.load(f)
            return data