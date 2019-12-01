from .base_spell import BaseSpell, BasePriestSpells


class GreaterHeal(BasePriestSpells):
    """
    Provides an interface to all the ranks of the Greater Heal spell
    """
    def __init__(self):
        self.rank1 = GreaterHealRank1()
        self.rank2 = GreaterHealRank2()
        self.rank3 = GreaterHealRank3()
        self.rank4 = GreaterHealRank4()
        self.rank5 = GreaterHealRank5()

    def _get_spells(self) -> list:
        """
        Internal method which returns an iterable list of spell rank objects
        """
        return [self.rank1, self.rank2, self.rank3, self.rank4, self.rank5]


class GreaterHealRank1(BaseSpell):
    """
    Data model for Greater Heal Rank 1
    """
    def __init__(self):
        self.cost = 370
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 924
        self.heal_high = 1039
        self.power_coef = 0.857
        self.spell_coef = 1.0
        self.name = 'Greater Heal (Rank 1)'


class GreaterHealRank2(BaseSpell):
    """
    Data model for Greater Heal Rank 2
    """
    def __init__(self):
        self.cost = 455
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 1178
        self.heal_high = 1318
        self.power_coef = 0.857
        self.spell_coef = 1.0
        self.name = 'Greater Heal (Rank 2)'


class GreaterHealRank3(BaseSpell):
    """
    Data model for Greater Heal Rank 3
    """
    def __init__(self):
        self.cost = 545
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 1470
        self.heal_high = 1642
        self.power_coef = 0.857
        self.spell_coef = 1.0
        self.name = 'Greater Heal (Rank 3)'


class GreaterHealRank4(BaseSpell):
    """
    Data model for Greater Heal Rank 4
    """
    def __init__(self):
        self.cost = 655
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 1813
        self.heal_high = 2021
        self.power_coef = 0.857
        self.spell_coef = 1.0
        self.name = 'Greater Heal (Rank 4)'


class GreaterHealRank5(BaseSpell):
    """
    Data model for Greater Heal Rank 5
    """
    def __init__(self):
        self.cost = 710
        self.cost_coef = 1.0
        self.cast = 3.0
        self.cast_coef = 1.0
        self.heal_low = 1966
        self.heal_high = 2194
        self.power_coef = 0.857
        self.spell_coef = 1.0
        self.name = 'Greater Heal (Rank 5)'
