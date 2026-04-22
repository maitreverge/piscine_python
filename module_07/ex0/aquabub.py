from ex0.creature import Creature


class Aquabub(Creature):
    """
    Creates an Aquabub Creature.
    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"
