from abc import ABC, abstractmethod


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