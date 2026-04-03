#! /usr/bin/python3


def input_temperature(temp_str: str) -> int:
    print(f"[Input data is {temp_str}]")
    return int(temp_str)


def test_temperature() -> None:
    valid_input: str = "25"
    invalid_input: str = "abc"

    # Try for a valid data
    try:
        result_1: int = input_temperature(valid_input)
    except Exception as e:
        print(f"Error in `input_temprature` : {e}")
    else:
        print(f"Temperature is now {result_1} °C")

    # Try for an invalid data
    try:
        result_2: int = input_temperature(invalid_input)
    except Exception as e:
        print(f"Error in `input_temprature` : {e}")
    else:
        print(f"Temperature is now {result_2} °C")


def main() -> None:
    """
    Main _1
    """
    test_temperature()


if __name__ == "__main__":
    main()
