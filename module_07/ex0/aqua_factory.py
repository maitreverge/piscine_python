from ex0.creature import Creature
from ex0.create_factory import CreatureFactory
from ex0.aquabub import Aquabub
from ex0.torragon import Torragon


class AquaFactory(CreatureFactory):
    """_Concrete factory for creating aqua creatures._"""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
