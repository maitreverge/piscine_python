#! /usr/bin/python3


def garden_operations(operation_number: int) -> None:
    print(f"testing operation {operation_number}")
    match operation_number:
        case 0:
            int("hey yo wtf")
        case 1:
            x: float = operation_number / 0
        case 2:
            open("nope.txt")
        case 3:
            y = operation_number + "Hello"  # mypy falsy line
        case _:
            print("All good here !")


def test_error_types() -> None:

    flasy_values: list[int] = list(range(-1, 6))

    for n in flasy_values:
        try:
            garden_operations(n)
        except ValueError as e:
            print(f"Value error detected for input {n} : {e}")
        except ZeroDivisionError as e:
            print(f"Zero division error detected for input {n} : {e}")
        except FileNotFoundError as e:
            print(f"File Not Found error detected for input {n} : {e}")
        except TypeError as e:
            print(f"TypeError error detected for input {n} : {e}")

    # Another way to catch all errors at once is to use base class `Exception`
    for n in flasy_values:
        try:
            garden_operations(n)
        except Exception as e:
            print(f"Catches all exception : {e}")


def main() -> None:
    """
    Main function
    """
    test_error_types()


if __name__ == "__main__":
    main()
