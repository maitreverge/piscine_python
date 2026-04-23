from typing import cast
from ex2.battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability

class AgressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            transformable = cast(TransformCapability, creature)
            return transformable.transform() + creature.attack() + transformable.revert()
        raise TypeError(f"Provided creature {creature.name} does not fit agressive strategy")
    
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature) and isinstance(creature, TransformCapability):
            return True
        return False