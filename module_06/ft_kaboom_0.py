#! /usr/bin/python3
"""
_module_doc_
"""

import alchemy.grimoire as grimoire


def main() -> None:
    """
    Main function
    """
    spell: str = "Fantasy"
    ingredients: str = "Earth, wind and fire"

    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record dark spell = ", end="")
    print(f"{grimoire.dark_spell_record(spell, ingredients)}")


if __name__ == "__main__":
    main()
