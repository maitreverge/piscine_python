#! /usr/bin/python3
"""
This modules emphasizes the importance of handling exceptions
and using the `with` statement for file operations.
"""


def secure_archive(
    file_name: str, file_mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    """
    Securely archives a file with the specified mode and content.

    Args:
        file_name (str): The name of the file to archive.
        file_mode (str, optional): The mode to open the file. Defaults to "r".
        content (str, optional): The content to write. Defaults to "".

    Returns:
        tuple[bool, str]: A tuple with the success and the data/error message.
    """
    operation_success: bool = False
    data: str = ""
    str_info = "regular"
    action: str = file_mode.lower().strip()
    try:
        # Check file_mode arg
        assert action in ["r", "w"]

        with open(file=file_name, mode=action, encoding="utf-8") as file:
            if action == "r":
                data = file.read()
                operation_success = True
            else:
                file.write(content)
                data = "Content successfully written to file"
                operation_success = True

    except FileNotFoundError as e:
        data = f"{e}"
        str_info = "non-existing"
    except PermissionError as e:
        data = f"{e}"
        str_info = "non-writable"
    except AssertionError as e:
        data = f"{e}"
        str_info = "wrong mode"
    except Exception as e:
        data = f"{e}"
        str_info = "unknown"

    operation = "read" if action == "r" else "write"
    print(f"Using `{file_name}` to {operation} ", end="")
    print(f"from a {str_info} file: ")
    return (operation_success, data)


def main() -> None:
    """
    Main function
    """
    # file_name: str = "./data.txt"
    # file_name: str = "data.txt"
    file_name = "dataaaaaaaaaa.txt"
    # file_mode: str = "r"
    # file_mode : str = "w"
    file_mode: str = "R   "
    # file_mode = "   W   "
    # file_mode = "hahahaha"
    content: str = "Content very interesting"
    print(secure_archive(file_name, file_mode, content))


if __name__ == "__main__":
    main()
