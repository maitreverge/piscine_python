from ex0.create_factory import CreatureFactory
from ex1.sproutling import Sproutling
from ex1.bloomelle import Bloomelle


class HealingCreatureFactory(CreatureFactory):
    """
    _Class Factory for Healing Capable Creatures_

    Args:
        CreatureFactory (_type_): _description_
    """

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
