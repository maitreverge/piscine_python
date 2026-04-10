#! /usr/bin/python3
"""
_module_doc_
"""

import alchemy.elements

def main() -> None:
    """
    Main function
    """
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...'structure", end='')
    print("Testing create_earth: ", end='')
    print(alchemy.elements.create_earth())
    

if __name__ == "__main__":
    main()

