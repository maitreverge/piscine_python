#! /usr/bin/python3
"""
_module_doc_
"""

import alchemy


def main() -> None:
    """
    Main function
    """
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion = {alchemy.strength_potion()}")
    print(f"Testing heal alias = {alchemy.heal()}")


if __name__ == "__main__":
    main()
