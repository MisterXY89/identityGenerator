
import random
import datetime
from identity import Identity
from generatorMath import GaussianChoice
from dataReader import DataReader

class Generator:
    def __init__(self):
        self.dataReader = DataReader()
        self.yearRange = range(1930, 2001)
        self.names = self.dataReader.getNames()
        self.heights = self.dataReader.getHeights()
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

    def genNationality(self):
        """ currently only one / DE """
        self.identity.nationality = "DE"

    def genHeight(self, sex):
        self.identity.height = self.heights[sex][self.gaussianChoice.getIndex(distribution = "c")]

    def genIdentity(self):
        self.genAge()
        self.genName(self.identity.birthYear)
        print("Name")
        self.genHeight(self.identity.sex)
        self.genNationality()
        self.identity.prettyPrint()

gen = Generator()
gen.genIdentity()
input()
