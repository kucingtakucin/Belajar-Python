#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:
    pass


hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.nama = 'Adam'
hero1.skill = 'tinju'
hero1.health = '100'
print(hero1)
print(hero1.__dict__)

hero2.nama = 'Arthur'
hero2.skill = 'pedang'
hero2.health = '250'
print(hero2)
print(hero2.__dict__)

hero3.nama = 'Mbah Putih'
hero3.skill = 'mage'
hero3.health = '500'
print(hero3)
print(hero3.__dict__)

print('\n')
print(copyright)
