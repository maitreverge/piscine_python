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

    def __init__(self, name: str, height: float, age: int, daily_growth: float) -> None:
        self._name = name.capitalize()
        self._initial_height = height
        self._current_height = self._initial_height
        self._age = age
        self._average_daily_growth = daily_growth

    def show(self) -> None:
        """
        Prints a summary of the plant name, height and age.
        """
        print(f"{self._name}: {round(self._current_height, 2)}cm, {self._age} days old")

    def grow(self, plant_mesure: float) -> None:
        """
        Update the `self._current_height`
        """
        self._current_height = plant_mesure
        self._age += 1

    def age(self, days_added: int) -> None:
        """
        Add `days_added` to `self._age` attribute.
        """
        self._age += days_added
        self._current_height += self._average_daily_growth * days_added


def ft_grow(plant: Plant, colors: dict) -> None:
    """
    Growth simulation only using `grow` method.
    This functions assumes the plants grows by 0.8cm each day.
    """
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(f"{colors["RED"]}", end="")
        plant.show()
        plant.grow(plant._current_height + 0.8)
        print(f"{colors["RESET"]}", end="")


def ft_age(plant: Plant, colors: dict) -> None:
    """
    Growth simulation only using `age` method.
    This functions assumes that one day is added at a time.
    """
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(f"{colors["GREEN"]}", end="")
        plant.show()
        plant.age(1)
        print(f"{colors["RESET"]}", end="")


def ft_age_and_growth(plant: Plant, colors: dict) -> None:
    """
    Growth simulation using `age` and `grow` method
    """
    print("=== Garden Plant Growth ===")


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

    ft_grow(plant_rose, colors)
    ft_age(plant_sunflower, colors)
    ft_age_and_growth(plant_cactus, colors)


if __name__ == "__main__":
    main()
