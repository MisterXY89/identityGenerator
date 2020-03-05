
import json
import pickle
import random
from random import randrange
from datetime import timedelta, datetime

class DataHandler:
    def __init__(self):
        self.filesPath = "files/"
        self.yearRangeFrom = 1930
        self.yearRangeTo = 2002
        self.names = f"{self.filesPath}names.pkl"
        # https://www.taschenhirn.de/geografie/groesste-deutsche-staedte/
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

    def _randomDate_func(self, start, end):
        """
        @author: nosklo, https://stackoverflow.com/a/553448
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def getRandomDate(self):
        d1 = datetime.strptime(f'1/1/{self.yearRangeFrom}', '%m/%d/%Y')
        d2 = datetime.strptime(f'1/1/{self.yearRangeTo}', '%m/%d/%Y')
        return self._randomDate_func(d1, d2)
