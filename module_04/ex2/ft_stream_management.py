#! /usr/bin/python3
"""
This module focuses on streams (stdin, stderr, stdout).
"""

import sys
from typing import IO


def get_file_obj() -> IO[str]:
    """
    Get the file object from the command line arguments.

    Raises:
        ArgvError: _if the number of arguments is not 2_

    Returns:
        IO[str]: _The file object_
    """
    if len(sys.argv) != 2:
        raise ValueError(
            "Wrong argument format.\nEx: ./ft_ancient_text.py <file_name>"
        )
    return open(sys.argv[1], "r", encoding="utf-8")


def access_data() -> str:
    """
    Acces the file given in `sys.argv[1]`, displays it and return the raw data.

    Returns:
        str: _file `str` object_
    """
    file_obj = get_file_obj()
    print("Accessing file ...\n---\n")
    file_data = file_obj.read()
    print(file_data)
    print("\n---\n")
    file_obj.close()
    print(f"File `{file_obj.name}` closed.")
    return file_data


def transform_data(file_data: str) -> None:
    """
    Displays file data with a trailing `#` at each end of line.
    Prompt user to write this new data in a filename of his choice.

    Args:
        file_data (str): _file `str` object_
    """
    # Split each line, and append `#\n` to each.
    splitted = file_data.split("\n")
    dict_transformed: list[str] = [x + "#\n" for x in splitted]

    # Reconstruct the whole string, and delete the trailing `\n`
    final_data = "".join(dict_transformed).rstrip("\n")

    print("Transform data:\n---\n")
    print(final_data)
    print("\n---\n")

    print("Enter a new file name to save this data ", end="")
    print("(Press `CTRL + D` to validate): ", end="", flush=True)

    # Used flushabove, otherwise message displas afterwards
    file_name: str = sys.stdin.read().strip()
    if not file_name:
        print("Data not saved.")
        return
    new_file_obj = open(file_name, "w", encoding="utf-8")
    print(f"Saving transformed data in {file_name}")
    new_file_obj.write(final_data)
    new_file_obj.close()


def main() -> None:
    """
    Main function
    """
    print("=== Cyber Archives Recovery ===")
    try:
        file_data = access_data()
        transform_data(file_data)
    except Exception as e:
        print(f"[STDERR]: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
