#  Copyright (c) 2020. Adam Arthur Faizal


class Hero:
    def __init__(self, name):
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.attack_power_pool = [0, 10, 20, 30, 40, 50]
        self.armor_pool = [1, 2, 3, 4, 5]
        self.__name = name
        self.__exp = 0
        self.__level = 0
        pass

    def info(self):
        print('{} \n\tLevel : {} \n\tHealth : {} \n\tAttack Power : {} \n\tArmor : {}'.format(
            self.__name,
            self.__level,
            self.__health,
            self.__attack_power,
            self.__armor
            )
        )
        pass

    @property
    def health_pool(self):
        pass

    @property
    def attack_power_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def level_up(self):
        pass

    @property
    def gain_exp(self):
        pass

    @health_pool.setter
    def health_pool(self, input):
        self.__health_pool = input

    @attack_power_pool.setter
    def attack_power_pool(self, input):
        self.__attack_power_pool = input

    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input

    @gain_exp.setter
    def gain_exp(self, input):
        self.__exp += input
        if self.__exp >= 100:
            self.level_up = self.__exp // 100
            self.__exp %= 100
            pass

    @level_up.setter
    def level_up(self, input):
        self.__level += input
        self.__health = self.health_pool[self.__level]
        self.__attack_power = self.attack_power_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        pass
    pass


class HeroIntelligent(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 50, 100, 150, 200, 250]
        self.attack_power_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 0.5, 1, 1.5, 2, 2.5]
        self.level_up = 1
        pass
    pass


class HeroStrength(Hero):
    def __init__(self, name):
        super(HeroStrength, self).__init__(name)
        self.health_pool = [0, 200, 400, 600, 800, 1000]
        self.attack_power_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 2, 4, 6, 8, 10]
        self.level_up = 1
        pass
    pass


adam = HeroIntelligent('Adam')
adam.info()
arthur = HeroStrength('Arthur')
arthur.info()
