#! /usr/bin/python3
"""
Focus on the 'import ...' structure to access the alchemy module.
This will show that only the functions defined in __init__.py are accessible,
and not the ones in elements.py
"""

import alchemy

def main() -> None:
    """
    Main function
    """
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print(f"Testing the hidden create_earth:")
    print(f"{alchemy.create_earth()}")
    

if __name__ == "__main__":
    main()

