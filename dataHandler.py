
import json
import pickle

class DataHandler:
    def __init__(self):
        self.filesPath = "files/"
        self.names = f"{self.filesPath}names.pkl"
        self.einwohner = f"{self.filesPath}einwohner.pkl"
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

    def getEinwohner(self):
        return self._load(self.einwohner)
