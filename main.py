from Power import Power
from Allegiance import Allegiance
from SuperHero import SuperHero

power1 = Power("Telekynésie")
print(power1.getName())
bad = Allegiance("Très méchant")
good = Allegiance("Super gentil")
print(bad.getName())
print(good.getName())
jad = SuperHero("Mighty JAD", '1974-04-16')
print(jad.getBirthDate())
print(jad.getAge())
jad.addPower(power1)
jad.addPower(Power("LaserEye"))
jad.addPower(Power("Fly"))
jad.addPower(Power("SuperStrength"))
jad.display()
