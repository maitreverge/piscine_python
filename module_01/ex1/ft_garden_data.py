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

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        """
        Prints a summary of the plant name, height and age.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """
    Main function
    """
    plant_1 = Plant("rose", 25, 30)
    plant_2 = Plant("sunflower", 80, 45)
    plant_3 = Plant("cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant_1.show()
    plant_2.show()
    plant_3.show()


if __name__ == "__main__":
    ft_garden_data()
