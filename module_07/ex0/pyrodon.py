from ex0.creature import Creature


class Pyrodon(Creature):
    """
    Creates a Pyrodon Creature.
    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"
