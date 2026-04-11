#! /usr/bin/python3
"""
_module_doc_
"""

from alchemy import potions


def main() -> None:
    """
    Main function
    """
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing healing_potion = {potions.healing_potion()}")
    print(f"Testing strength_potion = {potions.strength_potion()}")


if __name__ == "__main__":
    main()
