from abc import abstractmethod
from .base_class import BaseClass
import model.spell


class Priest(BaseClass):

    def __init__(self):
        super().__init__()
        self.int = 10
        self.spirit = 10
        self.mp5 = 1
        self.talent_points_spent = 1

        # Iterate over all of the Priest Spells in model.spell package
        for spell in model.spell.priest_spells.values():
            name = spell.__name__
            self.__setattr__(name, spell())


