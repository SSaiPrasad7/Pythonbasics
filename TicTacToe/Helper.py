import json

class Helper:
    def readConfig(self,filename):
        with open(filename, encoding='utf-8') as f:
            data=json.load(f)
            return data