from abc import abstractmethod
from .base_class import BaseClass


class Priest(BaseClass):

    def __init__(self):
        super().__init__()
        self.int = 10
        self.spirit = 10
        self.mp5 = 1
        self.talent_points_spent = 1
