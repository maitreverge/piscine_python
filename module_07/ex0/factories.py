#! /usr/bin/python3
"""
_This module focuses on the Abstract Factory Design Pattern_

"""

from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


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


class FlameFactory(CreatureFactory):
    """_Concrete factory for creating flame creatures._"""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """_Concrete factory for creating aqua creatures._"""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
