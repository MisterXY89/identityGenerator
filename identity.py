
class Identity:
    def __init__(self, sex):
        self.sex = sex
        self.name = ""
        self.birthYear = 0
        self.nationality = ""
        self.height = ""
        self.weight = ""

    def prettyPrint(self):
        print(vars(self))

    def json(self):
        return vars(self)
