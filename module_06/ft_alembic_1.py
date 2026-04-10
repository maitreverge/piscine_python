#! /usr/bin/python3
"""
Focus on the 'from ... import ...' structure to access the elements.py file.
"""

from elements import create_water

def main() -> None:
    """
    Main function
    """
    print("=== Alembic 1 ===")
    print("Using:'from ... import ...'structure to access elements.py", end='')
    print("Testing create_water: ", end='')
    print(create_water())
    

if __name__ == "__main__":
    main()
