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
        if height < 0 or age < 0 or daily_growth < 0:
            raise ValueError("Negative height / age / daily_growth provided.")

        self._name = name.capitalize()
        self._height = height
        self._initial_height = self._height
        self._age = age
        self._average_daily_growth = daily_growth

        print(f"Plant created: {self.show()}")

    def get_height(self) -> float:
        """
        Returns the plant's height.
        """
        return self._height

    def set_height(self, height: float) -> None:
        """
        Sets the plant's height.
        """
        if height < 0:
            print(f"Invalid given height of {height} for {self._name}")

            # Check if set_height has been called for the first time.
            try:
                if self._height:
                    pass  # Keep self._height untouched
            except Exception as e:
                print(f"Error {e}")
                print(f"Initiating {self._name} at 0")
                self._height = 0
            return

        self._height = height
        print(f"{self._name} heigh updated : {height}cm")

    def get_age(self) -> int:
        """
        Returns the plant's age.
        """
        return self._age

    def set_age(self, age: int) -> None:
        """
        Sets the plant's age.
        """
        if age < 0:
            print(f"Invalid given height of {age} for {self._name}")

            # Check if set_age has been called for the first time.
            try:
                if self._age:
                    pass  # Keep self._age untouched
            except Exception as e:
                print(f"Exception : {e}")
                print(f"Initiating {self._name} at 0")
                self._age = 0
            return

        self._age = age
        print(f"{self._name} age updated : {age} days old.")

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

    print("=== Garden Security System ===")
    plant_rose = Plant("rose", 25, 30, 0.8)

    plant_rose.set_age(2)
    plant_rose.set_age(20)
    plant_rose.set_age(-20)
    print(f"{plant_rose._name} age : {plant_rose.get_age()}")

    plant_rose.set_height(100)
    print(f"{plant_rose._name} height after update: {plant_rose.get_height()}")

    plant_rose.set_height(-14)
    print(f"{plant_rose._name} after falsy update: {plant_rose.get_height()}")

    # Trying faly init values leveraging try/except.
    try:
        age: int = -10  # False value
        height: float = 90  # False value
        daily_growth: float = 10
        plant_cactus = Plant("cactus", height, age, daily_growth)
        print(f"{plant_cactus.show()}")
    except ValueError as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
