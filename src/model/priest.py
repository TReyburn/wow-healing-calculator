from abc import abstractmethod
from .base_class import BaseClass


class BasePriest(BaseClass):

    @abstractmethod
    def _get_spells(self) -> list:
        pass

    def get_hps(self) -> dict:
        hps_dict = {}
        for spell in self._get_spells():
            hps_dict[spell.name] = spell.heal_high / spell.cast
        return hps_dict
