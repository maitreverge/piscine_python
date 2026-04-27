#! /usr/bin/python3
"""
_module_doc_
"""

import os
import site
import sys


def is_virtual_env_os() -> bool:
    """
    Detects virtual env by getting the `VIRTUAL_ENV`

    # ! NOTE : This function is here for demonstrating getting this piece of
    # ! info by another module. This solution is the less relaible, since
    # ! shell env can be modified elsewhere in the system.

    Returns:
        bool: _Is the programs runs in a venv_
    """
    result = os.getenv("VIRTUAL_ENV")
    return result is not None


def is_virtual_env_sys() -> bool:
    """
    Detects virtual env by comparing `sys.base_prefix != sys.prefix`
    False otherwise.

    Returns:
        bool: _Is the programs runs in a venv_
    """
    return sys.base_prefix != sys.prefix


def explain_env() -> None:
    """
    _Explain to muggle people hot to create a virtual env_
    """
    print("Program DOES NOT runs in a virtual env")
    print("=== HOW TO CREATE A VIRTUAL ENV ===")
    print("===")
    print("Run the command\n\npython3 -m venv `name_of_virtual_environment")
    print("Example:\n\tpython3 -m venv .venv")
    print(
        "After, activate the virtual env by running the command\n\n"
        "source `name_of_virtual_environment`/bin/activate"
    )
    print("Example:\n\tsource .venv/bin/activate")
    print("===")
    print("Welcome to Hogwarts dear wizard 🪄\n")


def main() -> None:
    """
    Main function
    """

    if is_virtual_env_sys():
        print("Program runs in a virtual env")
    else:
        explain_env()

    print(f"\nCurrent Python binary is located at `{sys.prefix}`")

    print("\nThose are the installed dependencies in this location :")
    packages = site.getsitepackages()
    for pack in packages:
        print(f"- {pack}")


if __name__ == "__main__":
    main()
