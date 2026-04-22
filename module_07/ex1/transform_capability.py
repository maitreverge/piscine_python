from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """
    _Class representing the ability to transform_

    Args:
        ABC (_type_): _Abstract Base Class_
    """

    @abstractmethod
    def transform(self) -> str:
        """
        _Turn Creature into a transformed mode,
        and modify `self.is_transformed` accordingly_

        Returns:
            str: _Transformation process_
        """

    @abstractmethod
    def revert(self) -> str:
        """
        _Turn Creature into a normal mode,
        and modify `self.is_transformed` accordingly_

        Returns:
            str: _Revert process_
        """
