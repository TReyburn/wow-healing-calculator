from abc import ABC, ABCMeta, abstractmethod


class SpellMeta(ABCMeta):
    required_attributes = []

    def __call__(cls):
        obj = super(SpellMeta, cls).__call__()
        for attribute_name in obj.required_attributes:
            if not getattr(obj, attribute_name):
                raise ValueError(f'Required attribute ({attribute_name}) not set')
        return obj


class BaseHeal(ABC, metaclass=SpellMeta):
    required_attributes = ['cost', 'cost_coef', 'cast', 'cast_coef', 'heal_low',
                           'heal_high', 'power_coef', 'spell_coef']

    def __repr__(self) -> str:
        my_dict = {}
        for attribute in self.required_attributes:
            my_dict[f'{attribute}'] = self.__getattribute__(attribute)
        return str(my_dict)
