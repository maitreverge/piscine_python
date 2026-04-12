#! /usr/bin/python3
"""
_module_doc_
"""

from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    """
    Main function
    """
    spell: str = "Fantasy"
    ingredients: str = "Earth, wind and fire"

    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Testing record dark spell = ", end="")
    print(f"{dark_spell_record(spell, ingredients)}")


if __name__ == "__main__":
    main()
