from typing import cast
from ex2.battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.heal_capability import HealCapability

class DefensiveStrategy(BattleStrategy):
    """
    _summary_

    Args:
        BattleStrategy (_type_): _description_
    """
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            transform = cast(HealCapability, creature)
            return creature.attack() + transform.heal()
        raise TypeError("Provided object is not of booth types `Creature` and `HealCapability")
        

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature) and isinstance(creature, HealCapability):
            return True
        return False