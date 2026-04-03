#! /usr/bin/python3
import sys


def main() -> None:
    """
    Main function
    """
    print("=== Command Quest ===")
    print(
        f"Program name: {sys.argv[0][2:]}"
    )  # Strip the `./` at the beggining

    # ! Alternate solution could be
    # print(f"Program name: {__file__.split('/')[-1]}")

    lenght_args: int = len(sys.argv)

    if lenght_args == 1:
        print("No argument provided !")
    else:
        print(f"Arguments recieved : {lenght_args - 1}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments : {lenght_args}")


if __name__ == "__main__":
    main()
