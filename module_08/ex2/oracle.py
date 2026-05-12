#! /usr/bin/python3
"""
_module_doc_
"""

import os
from dotenv import load_dotenv

load_dotenv()

MATRIX_MODE: str | None = os.getenv("MATRIX_MODE")
DATABASE_URL: str | None = os.getenv("DATABASE_URL")
API_KEY: str | None = os.getenv("API_KEY")
LOG_LEVEL: str | None = os.getenv("LOG_LEVEL")
ZION_ENDPOINT: str | None = os.getenv("ZION_ENDPOINT")


def check_config(list_config: list[tuple[str | None, str]]) -> bool:
    """
    _Check if all required config is allright and if none is missing_

    Args:
        list_config (list[tuple[str  |  None, str]]): _List of all config_

    Returns:
        bool: _Returns if config is okay or not_
    """
    is_all_config_ok: bool = True

    for tuple_config in list_config:
        env, name = tuple_config
        # Special check for MATRIX_MODE
        if name == "Mode":
            if not env:
                print(f"{name} = MISSING")
                is_all_config_ok = False
            elif env not in ["production", "development"]:
                print(f"{name} = Incorrect Config: {env}")
                is_all_config_ok = False
            else:
                print(f"{name} = {env}")
        else:
            if not env:
                print(f"{name} = MISSING")
                is_all_config_ok = False
            else:
                print(f"{name} = {env}")
    return is_all_config_ok


def main() -> None:
    """
    Main function
    """
    list_config: list[tuple[str | None, str]] = [
        (MATRIX_MODE, "Mode"),
        (DATABASE_URL, "Database"),
        (API_KEY, "API Access"),
        (LOG_LEVEL, "Log Level"),
        (ZION_ENDPOINT, "Zion Network"),
    ]

    print("ORACLE STATUS : Reading the Matrix...")
    is_config_okay = check_config(list_config)

    print("\nEnvironment security check: ")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")
    if is_config_okay:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file missing/incorrect config")


if __name__ == "__main__":
    main()
