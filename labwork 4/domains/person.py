class person:
    def __init__(self, name, DoB):
        self.validateName(name)
        self.validateDoB(DoB)

        self._name = name
        self._DoB = DoB

    def setName(self, name):
        self.validateName(name)
        self._name = name

    def getName(self):
        return self._name
    
    def validateName(self, name):
        if not isinstance(name, str):
            raise TypeError("Type of is not valid")
        elif len(name) < 0 or len(name) > 100:
            raise Exception("Name is not valid")
        

    def setDoB(self, DoB):
        self.validateDoB(DoB)
        self._DoB = DoB

    def getDOB(self):
        return self._DoB
    
    def validateDoB(self, DoB):
        if not isinstance(DoB, str):
            raise TypeError("Type is not valid")
        elif len(DoB) < 0:
            raise Exception("DoB id is not valid")


        