#! /usr/bin/python3
import sys
from typing import IO


class ArgvError(Exception):
    """
    

    Args:
        Exception (_type_): _description_
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


def get_file_obj() -> IO[str]:
    """
    Get the file object from the command line arguments.

    Raises:
        ArgvError: _if the number of arguments is not 2_

    Returns:
        IO[str]: _The file object_
    """
    if len(sys.argv) != 2:
        raise ArgvError(
            "Wrong argument format.\nEx: ./ft_ancient_text.py <file_name>"
        )
    return open(sys.argv[1], "r")


def main() -> None:
    """
    Main function
    """
    print("=== Cyber Archives Recovery ===")
    try:
        file_obj = get_file_obj()
        print("Accessing file ...\n---\n")
        print(file_obj.read())
        print("\n---\n")
        file_obj.close()
        print(f"File `{file_obj.name}` closed.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
