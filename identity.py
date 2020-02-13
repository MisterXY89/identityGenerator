
import json

class Identity:
    def __init__(self, sex):
        self.sex = sex

    def print(self):
        print(vars(self))

    def json(self):
        return json.dumps(vars(self))

    def getAsDict(self):
        return vars(self)
