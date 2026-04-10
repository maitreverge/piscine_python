#! /usr/bin/python3
"""
Focus on the 'from ... import ...' structure to access the alchemy module.
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

