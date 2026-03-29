#! /usr/bin/python3


class Plant:
    """
    Represents a plant with a name, height, and age.

    Attributes:
        name (str): The plant's name, capitalized.
        height (int): The plant's height in centimeters.
        age (int): The plant's age in days.

    Args:
        name (str): The plant's name (will be capitalized).
        height (int): The plant's height in centimeters.
        age (int): The plant's age in days.
    """

    def __init__(
        self, name: str, height: float, age: int, daily_growth: float
    ) -> None:
        self._name = name.capitalize()
        self._initial_height = height
        self._current_height = self._initial_height
        self._age = age
        self._average_daily_growth = daily_growth

    def show(self, color: str | None = None) -> None:
        """
        Prints a summary of the plant name, height and age.
        """
        print(f"{color}", end="")
        print(f"{color}{self._name}: ", end="")
        print(f"{round(self._current_height, 2)}cm, {self._age} days old")
        print("\033[0m", end="")  # Reset ANSII code

    def grow(self, plant_mesure: float) -> None:
        """
        This function updates the mesured height of the plant.
        """
        self._current_height = plant_mesure
        self._age += 1

    def age(self, days_added: int) -> None:
        """
        Adds `days_added` to the plant's age.
        Also udpdate its `self._average_daily_growth` by the days added.
        """
        self._age += days_added
        self._current_height += self._average_daily_growth * days_added


def main() -> None:
    """
    Main function
    """
    colors: dict = {
        "RESET": "\033[0m",
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
    }

    plant_rose = Plant("rose", 25, 30, 0.8)
    plant_sunflower = Plant("sunflower", 80, 45, 1.5)
    plant_cactus = Plant("cactus", 15, 120, 0.1)


if __name__ == "__main__":
    main()
