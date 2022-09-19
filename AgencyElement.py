import Agency


class AgencyElement:
    __name: str
    __agencies: [Agency]

    def __init__(self, name: str):
        self.__name = name
        self.__agencies=[]

    def getName(self) -> str:
        return self.__name

    def addAgency(self, agency:Agency):
        if agency not in self.__agencies:
            self.__agencies.append(agency)