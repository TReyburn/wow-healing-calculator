from abc import ABC, abstractmethod
from priest import BasePriest


class Heal(BasePriest):
    def __init__(self):
        self.rank1 = HealRank1()
        self.rank4 = HealRank4()


class BaseHeal(ABC):

    def __init__(self):
        self.cost = 1
        self.cost_coef = 1.0
        self.cast = 1.0
        self.cast_coef = 1.0
        self.heal_low = 1
        self.heal_high = 1
        self.power_coef = 1.0
        self.spell_coef = 1.0

    # @abstractmethod
    # def set_spell_coef(self, coef):
    #     self.spell_coef += coef


class HealRank1(BaseHeal):

    def __init__(self):
        self.cost = 155
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 307
        self.heal_high = 353
        self.power_coef = 0.729
        self.spell_coef = 1.0


class HealRank2(BaseHeal):

    def __init__(self):
        self.cost = 205
        self.cast_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0



class HealRank4(BaseHeal):

    def __init__(self):
        self.cost = 305
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 734
        self.heal_high = 827
        self.power_coef = 0.857
        self.spell_coef = 1.0
