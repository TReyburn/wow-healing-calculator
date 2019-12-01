from abc import ABC, abstractmethod


class BaseClass(ABC):

    @abstractmethod
    def _get_spells(self) -> list:
        pass
