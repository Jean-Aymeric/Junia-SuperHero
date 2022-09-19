import datetime
from AgencyElement import AgencyElement
from datetime import date, datetime
from Power import Power


class SuperHero(AgencyElement):
    __birthDate: date
    __powers: [Power]
    __teams: []

    def __init__(self, name: str, birthDate: date):
        AgencyElement.__init__(self, name)
        self.__birthDate = datetime.strptime(birthDate, "%Y-%m-%d")
        self.__powers = []
        self.__teams = []

    def getBirthDate(self) -> date:
        return self.__birthDate

    def getAge(self) -> int:
        return date.today().year - self.__birthDate.year - ((date.today().month, date.today().day) < (self.__birthDate.month, self.__birthDate.day))

    def addPower(self, power: Power):
        self.__powers.append(power)

    def display(self):
        print(self.getName() + " (", end="")
        for power in self.__powers:
            print(power.getName() + " ", end="")
        print(")")
        for team in self.__teams:
            print("\t-", team.getName())

    def getPowers(self) -> str :
        powers = ""
        for power in self.__powers:
            powers += power.getName() + ", "
        return powers

    def addTeam(self, team):
        if team not in self.__teams:
            self.__teams.append(team)
            team.addSuperHero(self)
