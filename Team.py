from AgencyElement import AgencyElement
from Allegiance import Allegiance
from SuperHero import SuperHero

class Team(AgencyElement):
    __superHeroes: [SuperHero]
    __allegiance: Allegiance


    def __init__(self, name: str, allegiance: Allegiance):
        AgencyElement.__init__(self, name)
        self.__allegiance = allegiance
        self.__superHeroes = []


    def getAllegiance(self) -> str:
        return self.__allegiance.getName()

    def addSuperHero(self,superHero: SuperHero):
        if superHero not in self.__superHeroes:
            self.__superHeroes.append(superHero)
            superHero.addTeam(self)

    def display(self):
        print(self.getName(),self.getAllegiance()," :")
        for superHero in self.__superHeroes:
            print("\t-",superHero.getName(),"(",superHero.getPowers(),")")