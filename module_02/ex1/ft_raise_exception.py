#! /usr/bin/python3


def input_temperature(temp_str: str) -> int:
    print(f"[Input data is {temp_str}]")
    result: int = int(temp_str)
    if result < 0 or result > 40:
        raise (ValueError("Temperature must be between 0 and 40 degres."))
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

    # Try valid temperatures
    print("Trying valid temperature")
    try:
        input_temperature("0")
        input_temperature("1")
        input_temperature("39")
        input_temperature("40")
    except Exception as e:
        print(f"Error in `input_temprature` : {e}")

    # Try invalid temperatures
    print("\nTrying invalid temperature 1/2")
    try:
        input_temperature("-1")
    except Exception as e:
        print(f"Error in `input_temprature` : {e}")

    print("\nTrying invalid temperature 2/2")
    try:
        input_temperature("41")
    except Exception as e:
        print(f"Error in `input_temprature` : {e}")


def main() -> None:
    """
    Main _1
    """
    test_temperature()


if __name__ == "__main__":
    main()
