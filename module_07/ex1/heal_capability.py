from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):  # pylint: disable=too-few-public-methods
    """
    _Class representing the ability to heal_

    Args:
        ABC (_type_): _Abstract Base Class_
    """

    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        """
        _Ability to heal itself or heal others creatures_

        Args:
            target (Creature | None, optional): _Creature to heal_.
            Defaults to None.

        Returns:
            str: _description_
        """
