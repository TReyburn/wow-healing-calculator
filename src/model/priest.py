from abc import ABC, abstractmethod


class BasePriest(ABC):

    @abstractmethod
    def _get_spells(self) -> list:
        pass
