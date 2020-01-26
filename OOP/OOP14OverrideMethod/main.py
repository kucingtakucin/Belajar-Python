#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        pass
    pass

    def info(self):
        print('Info di class Hero')
        print('Name : {} \nHealth : {}'.format(self.name, self.health))
        pass


class HeroIntelligent(Hero):
    def __init__(self, name):
        super(HeroIntelligent, self).__init__(name, 100)
        pass
    pass

    # Override
    def info(self):
        print('Info di sub-class HeroIntelligent')
        print('Name : {} \nTipe : Intelligent \nHealth : {}'.format(self.name, self.health))
        pass


class HeroStrength(Hero):
    def __init__(self, name):
        super(HeroStrength, self).__init__(name, 200)
        pass
    pass


adam = HeroIntelligent('Adam Arthur Faizal')
adam.info()
print('\n')
arthur = HeroStrength('Mbah Putih Mulyosugito')
arthur.info()

print('\n')
print(copyright)
