from ex0.creature import Creature
from ex1.transform_capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if not self.is_transformed:
            return f"{self.name} attacks normally !"
        return f"{self.name} performs a boosted strike !"

    def transform(self) -> str:
        if not self.is_transformed:
            self.is_transformed = True
            return f"{self.name} shift into a sharper form !"
        return f"{self.name} is already transformed !"

    def revert(self) -> str:
        if self.is_transformed:
            self.is_transformed = False
            return f"{self.name} returns to normal."
        return f"{self.name} is not transformed yet !"
