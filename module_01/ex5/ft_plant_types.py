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


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth: float,
        color: str,
    ) -> None:
        super().__init__(name, height, age, daily_growth)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        if self._is_blooming:
            print(f"[{self._name} is already blooming]")
            return
        print(f"[asking the {self._name.lower()} to bloom]")
        self._is_blooming = True

    def show(self) -> str:
        blooming_info: str = f"\n{self._name} "
        blooming_info += (
            "is blooming beautifully!"
            if self._is_blooming
            else "has not bloomed yet!"
        )
        extra_attributes: str = f"\nColor: {self._color}" + blooming_info
        return super().show() + extra_attributes


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth: float,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age, daily_growth)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of ")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide")

    def show(self) -> str:
        extra_attributes: str = f"\nTrunck diameter = {self._trunk_diameter}cm"
        return super().show() + extra_attributes


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth: float,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age, daily_growth)
        self._harvest_season = harvest_season
        self._nutritional_value = 0  # Ask in the subject

    def show(self) -> str:
        harvest_info: str = f"\nHarvest season: {self._harvest_season}"
        nutrition_info: str = f"\nNutritional value: {self._nutritional_value}"
        extra_attributes: str = harvest_info + nutrition_info
        return super().show() + extra_attributes

    def age(self, days_added: int) -> None:
        super().age(days_added)
        self._nutritional_value += 1

    def grow(self, plant_mesure: float) -> None:
        super().grow(plant_mesure)
        self._nutritional_value += 1


def main() -> None:
    """
    Main function
    """
    plant_tree = Tree("oak", 180, 2, 0.5, 12)

    print(plant_tree.show())
    print("-----------")
    plant_flower = Flower("rose", 12, 12, 0.5, "red")
    print(plant_flower.show())
    plant_flower.bloom()
    print(plant_flower.show())


if __name__ == "__main__":
    main()
