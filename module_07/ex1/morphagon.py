from ex0.creature import Creature
from ex1.transform_capability import TransformCapability


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if not self.is_transformed:
            return f"{self.name} attacks normally !"
        return f"{self.name} unleashes a devastating morph strike !"

    def transform(self) -> str:
        if not self.is_transformed:
            self.is_transformed = True
            return f"{self.name} morphs into a dragonic battle form !"
        return f"{self.name} is already transformed !"

    def revert(self) -> str:
        if self.is_transformed:
            self.is_transformed = False
            return f"{self.name} stabilizes its form."
        return f"{self.name} is not transformed yet !"
