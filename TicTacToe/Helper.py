import json

class Helper:
    def readConfig(fileName):
        with open(fileName) as f:
            return json.loads(f)