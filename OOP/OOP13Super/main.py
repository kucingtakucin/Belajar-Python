#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:

    def __init__(self, name, health):
        self.__name = name
        self.__health = health
        pass

    def info(self):
        print('{} dengan health {} '.format(self.__name, self.__health))
        pass
    pass


class HeroIntelligent(Hero):

    def __init__(self, name):
        super().__init__(name, 100)
        super().info()
        pass
    pass


class HeroStrength(Hero):

    def __init__(self, name):
        super(HeroStrength, self).__init__(name, 200)
        super(HeroStrength, self).info()
        pass
    pass


adam = HeroIntelligent('Adam')
arthur = HeroStrength('Arthur')

print('\n')
print(copyright)
