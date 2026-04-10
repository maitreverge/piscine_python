#! /usr/bin/python3
"""
_module_doc_
"""

from alchemy import elements

def main() -> None:
    """
    Main function
    """
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using ", end='')
    print("'from ... import ...'structure", end='')
    print("Testing create_air: ", end='')
    print(elements.create_air())
    

if __name__ == "__main__":
    main()

