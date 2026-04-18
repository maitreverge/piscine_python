#! /usr/bin/python3
"""
_This module focuses on the Abstract Factory Design Pattern_
"""

from abc import ABC, abstractmethod


class Creature(ABC):
    """
    Abstract base class for all creatures.

    Args:
        ABC (_type_): Abstract Base Class
    """

    def __init__(self, input_name: str, input_type: str) -> None:
        self.name = input_name
        self.type = input_type
        self.attack_name = ""

    @property
    def attack_name(self) -> str:
        return self._attack_name

    @attack_name.setter
    def attack_name(self, input_attack_name: str) -> None:
        if not isinstance(input_attack_name, str):
            raise TypeError(
                f"input attack name must be `str`, got `{type(input_attack_name)}`"
            )
        self._attack_name = input_attack_name

    @property
    def name(self) -> str:
        """
        _Get the name of the creature._
        Returns:
            str: The name of the creature.
        """
        return self._name

    @name.setter
    def name(self, input_name: str) -> None:
        """
        _Set the name of the creature._

        Args:
            input_name (str): The name to set for the creature.

        Raises:
            TypeError: If the input name is not a string.
        """
        if not isinstance(input_name, str):
            raise TypeError(
                f"input name must be `str`, got `{type(input_name)}`"
            )
        self._name = input_name

    @property
    def type(self) -> str:
        """
        _Get the type of the creature._
        Returns:
            str: The type of the creature.
        """
        return self._type

    @type.setter
    def type(self, input_type: str) -> None:
        """
        _Set the type of the creature._

        Args:
            input_type (str): The type to set for the creature.

        Raises:
            TypeError: If the input type is not a string.
        """
        if not isinstance(input_type, str):
            raise TypeError(
                f"input type must be `str`, got `{type(input_type)}`"
            )
        self._type = input_type

    @abstractmethod
    def attack(self) -> str:
        """
        _Abstract method to perform an attack._

        Returns:
            str: A string describing the attack action.
        """

    def describe(self) -> str:
        """
        _Describe the creature._

        Returns:
            str: A string describing the creature.
        """
        return f"Creature `{self._name}` is of type `{self._type}`"


class Flameling(Creature):
    """
    Creates a Flameling Creature.

    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")
        self.attack_name = "Ember"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"


class Pyrodon(Creature):
    """
    Creates a Pyrodon Creature.
    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")
        self.attack_name = "Flamethrower"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"


class Aquabub(Creature):
    """
    Creates an Aquabub Creature.
    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")
        self.attack_name = "Water Gun"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"


class Torragon(Creature):
    """
    Creates a Torragon Creature.
    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")
        self.attack_name = "Hydro Pump"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"
