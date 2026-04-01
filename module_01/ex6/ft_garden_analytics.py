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

    # ! A static method can't access the class methods neither attributes
    @staticmethod
    def is_older_one_year(age_input: int) -> bool:
        return age_input > 365

    # ! A class method
    @classmethod
    def create_anonymous_plant(cls, *args, **kwargs):
        return cls("Unkown", 0, 0, 0, *args, **kwargs)

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

    def grow(self, added_height: float) -> None:
        """
        This function updates the mesured height of the plant.
        """
        print(f"[Plant {self._name.lower()} growed of {added_height}cm(s)]")
        self._height += added_height
        self._age += 1

    def age(self, days_added: int) -> None:
        """
        Adds `days_added` to the plant's age.
        Also udpdate its `self._average_daily_growth` by the days added.
        """
        print(f"[Plant {self._name.lower()} aged of {days_added} day(s) old]")
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
        """
        Makes the flower bloom.
        """
        if self._is_blooming:
            print(f"[{self._name} is already blooming]")
            return
        print(f"[asking the {self._name.lower()} to bloom]")
        self._is_blooming = True

    def show(self) -> str:
        """
        Returns a summary of the name, height, age, and blooming status.

        Returns:
            str: A string containing the flower's information.
        """
        blooming_info: str = f"\n{self._name} "
        blooming_info += (
            "is blooming beautifully!"
            if self._is_blooming
            else "has not bloomed yet!"
        )
        extra_attributes: str = f"\nColor: {self._color}" + blooming_info
        return super().show() + extra_attributes


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth: float,
        color: str,
    ) -> None:
        super().__init__(
            name,
            height,
            age,
            daily_growth,
            color,
        )
        self._seeds = 0
    
    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42  # Hardcoded value, might change later.

    def show(self) -> str:
        extra_attributes: str = f"\nSeeds: {self._seeds}"
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
        """
        Makes the tree produce shade.
        """
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide")

    def show(self) -> str:
        """
        Returns a summary of the tree's name, height, age, and trunk diameter.

        Returns:
            str: A string containing the tree's information.
        """
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
        """
        Returns a summary of the vegetable's name, height, age,
        harvest season, and nutritional value.

        Returns:
            str: A string containing the vegetable's information.
        """
        harvest_info: str = f"\nHarvest season: {self._harvest_season}"
        nutrition_info: str = f"\nNutritional value: {self._nutritional_value}"
        extra_attributes: str = harvest_info + nutrition_info
        return super().show() + extra_attributes

    def age(self, days_added: int) -> None:
        """
        Ages the vegetable by the specified number of days.

        Args:
            days_added (int): The number of days to add to the vegetable's age.
        """
        super().age(days_added)
        self._nutritional_value += 1

    def grow(self, added_height: float) -> None:
        """
        Makes the vegetable grow by the specified height.

        Args:
            added_height (float): The height to add to the
            vegetable's current height.
        """
        super().grow(added_height)
        self._nutritional_value += 1


def main() -> None:
    """
    Main function
    """
    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant_flower = Flower("rose", 12, 12, 0.5, "red")

    # Checking @staticmethod
    age_to_check: int = 300
    if plant_flower.is_older_one_year(age_to_check):
        print(f"{age_to_check} is over 1 year old")
    else:
        print(f"{age_to_check} is NOT over 1 year old")

    # Checking @classmethod
    try:
        plant_tree = Tree.create_anonymous_plant()
        print(plant_tree.show())
    except Exception as e:
        print(f"Failed because {e}")


if __name__ == "__main__":
    main()
