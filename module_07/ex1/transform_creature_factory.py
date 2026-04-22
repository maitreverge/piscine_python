from ex0.create_factory import CreatureFactory
from ex1.shiftling import Shiftling
from ex1.morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):
    """
    _Class Factory for Healing Capable Creatures_

    Args:
        CreatureFactory (_type_): _description_
    """

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
