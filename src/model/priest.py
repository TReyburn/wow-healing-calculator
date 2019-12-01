from abc import abstractmethod
from .base_class import BaseClass


class BasePriest(BaseClass):

    @abstractmethod
    def _get_spells(self) -> list:
        pass
