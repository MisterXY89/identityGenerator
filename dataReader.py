
import pickle

class DataReader:
    def __init__(self):
        self.names = "infoCrawler/files/names.pkl"
        self.height = {
            "f": list(range(150, 165+35)),
            "m": list(range(165, 165+35))
        }

    def _load(self, file):
        return pickle.load(open(file, "rb"))

    def getNames(self):
        return self._load(self.names)

    def getHeights(self):
        return self.height
