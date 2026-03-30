#! /usr/bin/python3


class Plant:
    """
    Represents a plant with a name, height, and age.

    Attributes:
        name (str): The plant's name, capitalized.
        height (int): The plant's height in centimeters.
        age (int): The plant's age in days.
        average_daily_growth (float): The plant's average daily growth.

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
        self.set_height(height)
        self.set_age(age)
        self._average_daily_growth = daily_growth

    def get_height(self) -> float:
        """
        Returns the plant's height.

        Returns:
            float: The plant's height in centimeters.
        """
        return self._height

    # @set_height.setter
    def set_height(self, height: float) -> None:
        """
        Sets the plant's height.
        Args:
            height (float): The plant's height in centimeters.
        """
        if height < 0:
            print(f"Invalid given height of {height}.\nSetting height at 0")
            self._height = 0
            return
        self._height = height
    
    def get_age(self) -> int:
        """
        Returns the plant's age.

        Returns:
            int: The plant's age in days.
        """
        return self._age
    
    def set_age(self, age: int):
        """
        Sets the plant's age.
        Args:
            age (int): The plant's age in days.
        """
        if age < 0:
            print(f"Invalid given age of {age}.\nSetting age at 0")
            self._age = 0
            return
        self._age = age

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

    plant_rose = Plant("rose", -25, 30, 0.8)
    # plant_sunflower = Plant("sunflower", 80, 45, 1.5)
    # plant_cactus = Plant("cactus", 15, 120, 0.1)

    print(plant_rose._name)


if __name__ == "__main__":
    main()
