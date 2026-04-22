from ex0.creature import Creature
from ex1.heal_capability import HealCapability

class Bloomelle(Creature, HealCapability):
    """
    _Creature with an healing capability_

    Args:
        Creature (_type_): _ABC Creature Class_
        HealCapability (_type_): _ABC healCapability Class_
    """

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self.name} heals itself for a large amount"
        return f"{self.name} heals {target.name} for a large amount"