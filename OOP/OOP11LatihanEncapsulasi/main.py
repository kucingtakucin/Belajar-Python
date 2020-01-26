#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:
    # Private class variable
    __jumlah = 0

    def __init__(self, name, health, attack_power, armor):
        self.__name = name
        self.__health_standar = health
        self.__attack_power_standar = attack_power
        self.__armor_standar = armor
        self.__level = 1
        self.__exp = 0

        self.__heatlh_max = self.__health_standar * self.__level
        self.__attack_power = self.__attack_power_standar * self.__level
        self.__armor = self.__armor_standar * self.__level

        self.__health = self.__heatlh_max
        Hero.__jumlah += 1
        pass

    @property
    def info(self):
        return "{} level {} : \n\t Health = {}/{} \n\t Attack = {} \n\t Armor = {} ".format(self.__name, self.__level, self.__health_standar, self.__health, self.__attack_power, self.__armor)
        pass

    @property
    def gain_exp(self):
        pass

    @gain_exp.setter
    def gain_exp(self, add_exp):
        self.__exp += add_exp
        if self.__exp >= 100:
            print(self.__name, 'LEVEL UP!')
            self.__level += 1
            self.__exp -= 100

            self.__heatlh_max = self.__health_standar * self.__level
            self.__attack_power = self.__attack_power_standar * self.__level
            self.__armor = self.__armor_standar * self.__level
            pass
        pass

    @property
    def attack(self):
        pass

    @attack.setter
    def attack(self, musuh):
        print(self, 'menyerang', musuh)
        self.gain_exp(50)
        pass


adam = Hero('Adam', 100, 5, 10)
print(adam.info)
arthur = Hero('Arthur', 100, 5, 10)
print(arthur.info)

adam.attack(arthur)
adam.attack(arthur)
adam.attack(arthur)

print('\n')
print(copyright)
