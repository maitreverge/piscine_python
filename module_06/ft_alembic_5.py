#! /usr/bin/python3
"""
_module_doc_
"""

from alchemy import elements

def main() -> None:
    """
    Main function
    """
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print("Testing create_air: ", end='')
    print(elements.create_air())
    

if __name__ == "__main__":
    main()

