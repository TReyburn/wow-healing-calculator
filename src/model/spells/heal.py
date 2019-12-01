from .base_spell import BaseSpell, BasePriestSpells


class Heal(BasePriestSpells):
    """
    Provides an interface to all the ranks of the Heal spell
    """
    def __init__(self):
        self.rank1 = HealRank1()
        self.rank2 = HealRank2()
        self.rank3 = HealRank3()
        self.rank4 = HealRank4()

    def _get_spells(self) -> list:
        """
        Internal method which returns an iterable list of spell rank objects
        """
        return [self.rank1, self.rank2, self.rank3, self.rank4]


class HealRank1(BaseSpell):
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
        self.name = 'Heal (Rank 1)'


class HealRank2(BaseSpell):
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
        self.name = 'Heal (Rank 2)'


class HealRank3(BaseSpell):
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
        self.name = 'Heal (Rank 3)'


class HealRank4(BaseSpell):
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
        self.name = 'Heal (Rank 4)'
