#! /usr/bin/python3
"""
_module_doc_
"""


def secure_archive(
    file_name: str, file_mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    operation_success: bool = False
    data: str = ""
    str_info = ""
    try:
        # Check file_mode arg
        action: str = file_mode.lower().strip()
        assert action in "r" or action == "w"

        with open(file_name, file_mode, encoding="utf-8") as file:
            if file_mode == "r":
                data = file.read()
            else:
                assert content != ""
                file.write(content)

    except Exception as e:
        data = f"{e}"

    finally:
        print(
            f"Using {file_name} to {"read" if file_mode == "r" else "write"}",
            end="",
        )
        print(f"from a {str_info} file: ")
        return (operation_success, data)


def main() -> None:
    """
    Main function
    """
    file_name: str = "data.txt"
    # file_name = "dataaaaaaaaaa.txt"
    file_mode: str = "r"
    # file_mode : str = "w"
    # file_mode = "R   "
    # file_mode = "   W   "
    # file_mode = "hahahaha"
    content: str = "Content very interesting"
    # content: str = ""
    secure_archive(file_name, file_mode, content)


if __name__ == "__main__":
    main()
