from abc import ABC, abstractmethod
from .meta_spell import SpellMeta


class BaseSpell(ABC, metaclass=SpellMeta):
    required_attributes = ['cost', 'cost_coef', 'cast', 'cast_coef', 'heal_low',
                           'heal_high', 'power_coef', 'spell_coef', 'name']

    def __str__(self) -> str:
        my_dict = {}
        for attribute in self.required_attributes:
            my_dict[f'{attribute}'] = self.__getattribute__(attribute)
        return str(my_dict)
