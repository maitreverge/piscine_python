from abc import ABC, abstractmethod
from ex0.creature import Creature


class CreatureFactory(ABC):
    """
    _Abstract base class for creature factories._
    Args:
        ABC (_type_): Abstract Base Class
    """

    @abstractmethod
    def create_base(self) -> Creature:
        """
        _Create a base creature._
        Returns:
            Creature: An instance of a base creature.
        """

    @abstractmethod
    def create_evolved(self) -> Creature:
        """
        _Create an evolved creature._
        Returns:
            Creature: An instance of an evolved creature.
        """
