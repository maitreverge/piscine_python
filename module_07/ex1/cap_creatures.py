#! /usr/bin/python3
"""
_module_doc_
"""

from .capabilities import HealCapability, TransformCapability
from ex0.creatures import Creature



class Sproutling(Creature, HealCapability):
    """
    _Creature with an healing capability_

    Args:
        Creature (_type_): _ABC Creature Class_
        HealCapability (_type_): _ABC healCapability Class_
    """

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")
        self.attack_name = "Vine Whip"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self.name} heals itself for a small amount"
        return f"{self.name} heals {target.name} for a small amount"


class Bloomelle(Creature, HealCapability):
    """
    _Creature with an healing capability_

    Args:
        Creature (_type_): _ABC Creature Class_
        HealCapability (_type_): _ABC healCapability Class_
    """

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")
        self.attack_name = "Vine Whip"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self.name} heals itself for a large amount"
        return f"{self.name} heals {target.name} for a large amount"


def main():
    sp = Sproutling()
    bl = Bloomelle()

    print(sp.heal(bl))
