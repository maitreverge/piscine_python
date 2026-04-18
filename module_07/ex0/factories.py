#! /usr/bin/python3
"""
_module_doc_
"""
from abc import abstractmethod
from creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon

class CreatureFactory(Creature):
    """
    _summary_

    Args:
        Flameling (_type_): _description_
        Pyrodon (_type_): _description_
        Aquabub (_type_): _description_
        Torragon (_type_): _description_
    """
    def __init__(self, input_name: str, input_type: str) -> None:
        super().__init__(input_name, input_type)
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling")
    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon")

class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Aquabub")
    def create_evolved(self) -> Creature:
        return Torragon("Torragon")