
import math
import random
import datetime
from identity import Identity
from generatorMath import GaussianChoice
from dataHandler import DataHandler

class Generator:
    def __init__(self):
        self.dataHandler = DataHandler()
        self.yearRange = range(1930, 2001)
        self.names = self.dataHandler.getNames()
        self.heights = self.dataHandler.getHeights()
        self.bmis = self.dataHandler.getBmis()
        self.gaussianChoice = GaussianChoice(35)
        self.sex = random.choice(["m", "f"])
        self.identity = Identity(self.sex)

    def genAge(self):
        self.identity.birthYear = random.choice(self.yearRange)
        self.identity.age = datetime.datetime.now().year - self.identity.birthYear

    def genName(self, birthYear):
        """ choose a name based on sex and birthYear """
        selector = "boys" if self.sex == "m" else "girls"
        namesByYear = self.names[str(birthYear)][selector]
        self.identity.name = namesByYear[self.gaussianChoice.getIndex()]

    def genWeight(self, sex, height):
        self.identity.bmi = self.bmis[sex][self.gaussianChoice.getIndex(distribution = "c")%5]
        self.identity.weight = format(float(self.identity.bmi * math.pow(height/100, 2)), '.1f')

    def genNationality(self):
        """ currently only one / DE """
        self.identity.nationality = "DE"

    def genHeight(self, sex):
        self.identity.height = self.heights[sex][self.gaussianChoice.getIndex(distribution = "c")%30]

    def genIdentity(self):
        self.genAge()
        self.genName(self.identity.birthYear)
        self.genHeight(self.identity.sex)
        self.genWeight(self.identity.sex, self.identity.height)
        self.genNationality()
        self.identity.prettyPrint()

gen = Generator()
gen.genIdentity()

input()
