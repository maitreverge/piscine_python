from ex2.battle_strategy import BattleStrategy
from ex0.creature import Creature

class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.attack()
        raise TypeError("Provided object is not of base type `Creature`")
    
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False