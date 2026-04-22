from abc import ABC, abstractmethod

class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.is_transformed: bool = False

    
    @abstractmethod
    def transform(self) -> str:
        ...
    
    @abstractmethod
    def revert(self) -> str:
        ...
    