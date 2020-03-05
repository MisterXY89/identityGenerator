
import math
import random
import datetime
from identity import Identity
from generatorMath import GaussianChoice
from dataHandler import DataHandler

class Generator:
    """
    Controller for the generation of an identity -
    provides all gen-methods and combines the data and logic.
    Currently only German identities can be generated.
    """
    def __init__(self):
        self.dataHandler = DataHandler()
        self.names = self.dataHandler.getNames()
        self.familyNames = self.dataHandler.getFamilyNames()
        self.heights = self.dataHandler.getHeights()
        self.bmis = self.dataHandler.getBmis()
        self.einwohner = self.dataHandler.getEinwohner()
        self.gaussianChoice = GaussianChoice(35)
        self.sex = random.choice(["m", "f"])
        self.identity = Identity(self.sex)

    def genAge(self):
        """ choose random age and calculate current age """
        date = self.dataHandler.getRandomDate()
        self.identity.birthYear = date.year
        self.identity.age = datetime.datetime.now().year - self.identity.birthYear
        self.identity.birthday = f"{date.day}.{date.month}"

    def genName(self, birthYear):
        """ choose a name based on sex and birthYear """
        selector = "boys" if self.sex == "m" else "girls"
        namesByYear = self.names[str(birthYear)][selector]
        self.identity.name = namesByYear[self.gaussianChoice.getIndex()]
        self.identity.familyName = self.familyNames[GaussianChoice(99).getIndex()]

    def genWeight(self, sex, height):
        """ generate weigt based on sex, height & the bmi and gaussian normal distribution """
        self.identity.bmi = self.bmis[sex][GaussianChoice(5).getIndex(distribution = "c")]
        # add 2 for a more realistic weight
        self.identity.weight = float(format(float(self.identity.bmi * math.pow(height/100, 2)), '.1f')) + 2

    def genNationality(self):
        """ currently only one / DE """
        self.identity.nationality = "DE"

    def genHeight(self, sex):
        """ generate height based on sex and gaussian normal distribution """
        self.identity.height = self.heights[sex][GaussianChoice(30).getIndex(distribution = "c")]

    def genCity(self):
        """ choose random city from one of the 80 biggest citys in germany """
        cityData = self.einwohner[GaussianChoice(80).getIndex()]
        self.identity.city = cityData["Stadt"]
        self.identity.state = cityData["bundesland"]

    def genIdentity(self):
        """ collection of all method calls in ordet to generate a random identity """
        self.genAge()
        self.genName(self.identity.birthYear)
        self.genHeight(self.identity.sex)
        self.genWeight(self.identity.sex, self.identity.height)
        self.genNationality()
        self.genCity()


gen = Generator()
gen.genIdentity()
gen.identity.print()
input()
