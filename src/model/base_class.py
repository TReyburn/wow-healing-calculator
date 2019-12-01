from abc import ABC, abstractmethod
from .meta_class import ClassMeta


class BaseClass(ABC, metaclass=ClassMeta):
    required_attributes = ['int', 'spirit', 'mp5', 'talent_points_spent', 'talent_points_max']

    @abstractmethod
    def __init__(self):
        self.talent_points_max = 52
