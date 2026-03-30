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
        if height < 0 or age < 0 :
            raise ValueError(f"Negative height or age provided.")
        
        self._name = name.capitalize()
        self._height = height
        self._initial_height = self._height

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        self.set_age(age)
        self._average_daily_growth = daily_growth
        print(f"Plant created: {self.show()}")

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
        print(f"\n{self._name} height update: ", end='')
        if height < 0:
            print(f"rejected.")
            print(f"Invalid given height of {height}")
            
            # Check if set_height has been called for the first time.
            try:
                if self._height:
                    print("Setting height at 0\n")
            except:
                print(f"Initiating {self._name} at 0")
                self._height = 0
            return
                
        print(f"{height}cm")
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
        print(f"{self._name} age update: ", end='')
        if age < 0:
            print(f"rejected.")
            print(f"Invalid given age of {age}")
            
            # Check if set_age has been called for the first time.
            try:
                if self._age:
                    print("Setting age at 0")
            except:
                print(f"Initiating {self._name} at 0")
                self._age = 0
            return
                
        print(f"{age} days old.")
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

    print("=== Garden Security System ===")
    plant_rose = Plant("rose", 25, 30, 0.8)

    plant_rose.set_age(2)
    plant_rose.set_age(20)
    plant_rose.set_age(-20)
    print(f"{plant_rose._name} age : {plant_rose.get_age()}")
    
    # print(f"Plant created: {plant_rose.show()}")


if __name__ == "__main__":
    main()
