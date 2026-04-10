#! /usr/bin/python3
"""
Focus on the 'from ... import ...' structure to access the elements.py file
from the alchemy package.
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

