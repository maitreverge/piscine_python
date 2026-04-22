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
        """
        _Get the name of the creature's attack._
        Returns:
            str: The name of the creature's attack.
        """
        return self._attack_name

    @attack_name.setter
    def attack_name(self, name_attack: str) -> None:
        """
        _Set the name of the creature's attack._
        Args:
            name_attack (str): The name to set for the creature's attack.
        Raises:
            TypeError: If the input attack name is not a string.
        """
        if not isinstance(name_attack, str):
            raise TypeError(
                f"input attack name must be `str`, got `{type(name_attack)}`"
            )
        self._attack_name = name_attack

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
        return f"Creature `{self.name}` is of type `{self.type}`"