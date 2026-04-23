from abc import ABC, abstractmethod
from ex0.creature import Creature


class BattleStrategy(ABC):
    """
    _summary_

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def act(self, creature: Creature) -> str:
        """
        _summary_
        """
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """
        _Returns a bool indicating that a `Creature` is suitable
        for the strategy_

        Returns:
            bool: _description_
        """