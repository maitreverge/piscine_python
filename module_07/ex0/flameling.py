from ex0.creature import Creature


class Flameling(Creature):
    """
    Creates a Flameling Creature.

    Args:
        Creature (_type_): Base class for all creatures.
    """

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"
