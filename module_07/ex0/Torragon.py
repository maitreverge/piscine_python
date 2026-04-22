from ex0.Creature import Creature

class Torragon(Creature):
    """
    Creates a Torragon Creature.
    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"