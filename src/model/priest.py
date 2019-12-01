from abc import abstractmethod
from .base_class import BaseClass
import model.spells


class Priest(BaseClass):

    def __init__(self):
        super().__init__()
        self.int = 10
        self.spirit = 10
        self.mp5 = 1
        self.talent_points_spent = 1
        self.spells = []
        self.level = 60

        # Iterate over all of the Priest Spells in model.spells package
        for spell in model.spells.priest_spells.values():
            name = spell.__name__
            self.__setattr__(name, spell())
            self.spells.append(name)


