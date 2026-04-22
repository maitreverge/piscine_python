from ex0.CreateFactory import CreatureFactory
from ex0.Creature import Creature
from ex0.Flameling import Flameling
from ex0.Pyrodon import Pyrodon


class FlameFactory(CreatureFactory):
    """_Concrete factory for creating flame creatures._"""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()