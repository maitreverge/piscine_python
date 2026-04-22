#! /usr/bin/python3
"""
_module_doc_
"""

from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory


def main() -> None:
    """
    Main function
    """
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    # Creating heal creatures
    sprout = heal_factory.create_base()
    bloom = heal_factory.create_evolved()

    # Creating transform creatures
    shift = transform_factory.create_base()
    morph = transform_factory.create_evolved()

    print("==== Testing Healing Capabilites ====")

    print("Base:")
    print(sprout.describe())
    print(sprout.attack())
    print(shift.attack())
    print(sprout.heal())

    print("\nEvolved:")
    print(bloom.describe())
    print(bloom.attack())
    print(bloom.heal())

    print("\n==== Testing Transform Capabilites ====")
    print("Base:")
    print(shift.describe())
    print(shift.attack())
    print(shift.transform())
    print(shift.transform())
    print(shift.attack())
    print(shift.revert())
    print(shift.revert())
    print(shift.attack())

    print("\nEvolved:")
    print(morph.describe())
    print(morph.attack())
    print(morph.transform())
    print(morph.transform())
    print(morph.attack())
    print(morph.revert())
    print(morph.revert())
    print(morph.attack())


if __name__ == "__main__":
    main()
