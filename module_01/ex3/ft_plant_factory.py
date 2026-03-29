#! /usr/bin/python3


class Plant:
    """
    Represents a plant with a name, height, and age.

    Attributes:
        name (str): The plant's name, capitalized.
        height (int): The plant's height in centimeters.
        age (int): The plant's age in days.
        average_daily_growth (float): The plant's average daily growth.
        initial_height (float): The plant's initial height in centimeters.

    Args:
        name (str): The plant's name (will be capitalized).
        height (int): The plant's height in centimeters.
        age (int): The plant's age in days.
        daily_growth (float): The plant's average daily growth in centimeters.
    """

    def __init__(
        self, name: str, height: float, age: int, daily_growth: float
    ) -> None:
        self._name = name.capitalize()
        self._initial_height = height
        self._height = self._initial_height
        self._age = age
        self._average_daily_growth = daily_growth

    def show(self) -> str:
        """
        Returns a summary of the plant name, height and age.
        """
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"

    def grow(self, plant_mesure: float) -> None:
        """
        This function updates the mesured height of the plant.
        """
        self._height = plant_mesure
        self._age += 1

    def age(self, days_added: int) -> None:
        """
        Adds `days_added` to the plant's age.
        Also udpdate its `self._average_daily_growth` by the days added.
        """
        self._age += days_added
        self._height += self._average_daily_growth * days_added


def main() -> None:
    """
    Main function
    """

    plant_rose = Plant("rose", 25, 30, 0.8)
    plant_sunflower = Plant("sunflower", 80, 45, 1.5)
    plant_cactus = Plant("cactus", 15, 120, 0.1)

    print("=== Plant Factory Output ===")
    print(f"Created: {plant_rose.show()}")
    print(f"Created: {plant_sunflower.show()}")
    print(f"Created: {plant_cactus.show()}")


if __name__ == "__main__":
    main()
