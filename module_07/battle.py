#! /usr/bin/python3
"""
_module_doc_
"""

from ex0 import FlameFactory, AquaFactory


def main() -> None:
    """
    Main function
    """
    print("=== Testing Flame Factories ===")

    # Flame factories
    flame_fact = FlameFactory()
    flame_base = flame_fact.create_base()
    flame_adv = flame_fact.create_evolved()

    print(flame_base.describe())
    print(flame_base.attack())
    print(flame_adv.describe())
    print(flame_adv.attack())
    print(flame_adv.attack())
    print(flame_adv.attack())

    # Aqua factories
    print("\n=== Testing Aqua Factories ===")
    aqua_fact = AquaFactory()

    aqua_base = aqua_fact.create_base()
    aqua_adv = aqua_fact.create_evolved()

    print(aqua_base.describe())
    print(aqua_base.attack())
    print(aqua_adv.describe())
    print(aqua_adv.attack())

    # print(aa.describe())


if __name__ == "__main__":
    main()
