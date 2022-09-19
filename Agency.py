class Agency:
    __name: str
    __agencyElements: []

    def __init__(self, name: str):
        self.__name = name
        self.__agencyElements = []

    def getName(self) -> str:
        return self.__name

    def getInfo(self) -> str:
        temp=self.__name
        for agencyElement in self.__agencyElements:
            temp+=" " + agencyElement.getName()
        return temp

    def addAgencyElement(self, agencyElement):
        if agencyElement not in self.__agencyElements:
            self.__agencyElements.append(agencyElement)
