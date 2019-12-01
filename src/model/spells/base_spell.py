from abc import ABC, abstractmethod
from .meta_spell import SpellMeta


class BaseSpell(ABC, metaclass=SpellMeta):
    required_attributes = ['cost', 'cost_coef', 'cast', 'cast_coef', 'heal_low',
                           'heal_high', 'power_coef', 'spell_coef', 'name']

    def __repr__(self) -> str:
        """
        A method for printing all attributes of a spell rank
        :return:
        """
        my_dict = {}
        for attribute in self.required_attributes:
            my_dict[f'{attribute}'] = self.__getattribute__(attribute)
        return str(my_dict)


class BasePriestSpells(ABC):
    """
    Creates a standard interface for all Priest spells
    """

    @abstractmethod
    def _get_spells(self) -> list:
        pass

    def get_hps(self) -> dict:
        hps_dict = {}
        for spell in self._get_spells():
            hps_dict[spell.name] = spell.heal_high / spell.cast
        return hps_dict
