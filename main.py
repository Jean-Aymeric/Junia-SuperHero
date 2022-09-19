from Agency import Agency
from Power import Power
from Allegiance import Allegiance
from SuperHero import SuperHero
from Team import Team

power1 = Power("Telekynésie")
print(power1.getName())
bad = Allegiance("Très méchant")
good = Allegiance("Super gentil")
print(bad.getName())
print(good.getName())
jad = SuperHero("Mighty JAD", '1974-04-16')
kento = SuperHero("Mega Kento", '2003-07-01')
Bflo = SuperHero("Big Flo", '1787-07-01')
FlashMcQueen = SuperHero("VROUMVROUM", '2003-01-01')
print(jad.getBirthDate())
print("age :", jad.getAge(), "ans")
print(kento.getBirthDate())
print("age :", kento.getAge(), "ans")
jad.addPower(power1)
jad.addPower(Power("LaserEye"))
jad.addPower(Power("Fly"))
jad.addPower(Power("SuperStrength"))
jad.display()
kento.addPower(Power("Invisibility"))
kento.addPower(Power("Spider-Super-Mega-Web"))
Bflo.addPower(Power("Gros"))
teamKento = Team("Kteam", good)
teamKento.addSuperHero(jad)
teamKento.addSuperHero(kento)
teamKento.display()
teambad = Team("BadTeam", bad)
teambad.addSuperHero(Bflo)
teambad.display()
jad.display()
speculos = Agency("speculos")
speculos.addAgencyElement(teamKento)
speculos.addAgencyElement(Bflo)

print(speculos.getInfo())
print("\t")
print("QUAND FLASH MC QUEEN ARRIVE IL FAIT ",FlashMcQueen.getName())
