#! /usr/bin/python3
"""
_module_doc_
"""

from ex1.sproutling import Sproutling
from ex1.bloomelle import Bloomelle


def main() -> None:
    """
    Main function
    """

    ss = Sproutling()

    bl = Bloomelle()
    print(bl.heal(ss))
    

if __name__ == "__main__":
    main()