
import json
import pickle

class DataHandler:
    def __init__(self):
        self.filesPath = "files/"
        self.names = f"{self.filesPath}names.pkl"
        self.einwohner = f"{self.filesPath}einwohner.pkl"
        self.einwohnerJ = f"{self.filesPath}einwohner.json"
        self.height = {
            "f": list(range(155, 185)),
            "m": list(range(165, 195))
        }
        self.bmis = {
            "f": list(range(19,25)),
            "m": list(range(20, 26))
        }

    def _load(self, file):
        return pickle.load(open(file, "rb"))

    def getNames(self):
        return self._load(self.names)

    def getHeights(self):
        return self.height

    def getBmis(self):
        return self.bmis

    def jsonLoad(self):
        with open(self.einwohnerJ) as json_data:
            d = json.load(json_data)
            print(d)
            pickle.dump(d, open(self.einwohner), "wb")



dr = DataHandler()
dr.jsonLoad()
