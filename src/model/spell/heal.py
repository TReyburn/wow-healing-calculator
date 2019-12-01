from .base_spell import BaseSpell
from ..priest import BasePriest


class Heal(BasePriest):
    """
    Provides an interface to all the ranks of Heal spell
    """
    def __init__(self):
        self.rank1 = SpellRank1()
        self.rank2 = SpellRank2()
        self.rank3 = SpellRank3()
        self.rank4 = SpellRank4()

    def _get_spells(self) -> list:
        """
        Internal method which returns an iterable list of spell rank objects
        """
        return [self.rank1, self.rank2, self.rank3, self.rank4]


class SpellRank1(BaseSpell):
    """
    Data model for Heal Rank 1
    """
    def __init__(self):
        self.cost = 155
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 307
        self.heal_high = 353
        self.power_coef = 0.729
        self.spell_coef = 1.0


class SpellRank2(BaseSpell):
    """
    Data model for Heal Rank 2
    """
    def __init__(self):
        self.cost = 205
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 445
        self.heal_high = 507
        self.power_coef = 0.857
        self.spell_coef = 1.0


class SpellRank3(BaseSpell):
    """
    Data model for Heal Rank 3
    """
    def __init__(self):
        self.cost = 255
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 586
        self.heal_high = 662
        self.power_coef = 0.857
        self.spell_coef = 1.0


class SpellRank4(BaseSpell):
    """
    Data model for Heal Rank 4
    """
    def __init__(self):
        self.cost = 305
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 734
        self.heal_high = 827
        self.power_coef = 0.857
        self.spell_coef = 1.0
