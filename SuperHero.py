import datetime
from AgencyElement import AgencyElement
from datetime import date, datetime


class SuperHero(AgencyElement):
    __birthDate: date

    def __init__(self, name: str, birthDate: date):
        AgencyElement.__init__(self, name)
        self.__birthDate = datetime.strptime(birthDate, "%Y-%m-%d")

    def getBirthDate(self) -> date:
        return self.__birthDate

    def getAge(self) -> int:
        return date.today().year - self.__birthDate.year - ((date.today().month, date.today().day) < (self.__birthDate.month, self.__birthDate.day))
