#! /usr/bin/python3
import math


def get_player_pos() -> tuple[float, float, float]:
    """
    Prompt user for coordinates

    Returns:
        tuple: x, y and z coordinates
    """
    while True:
        try:
            usr_input: str = input(
                "Enter new coordinates as floats in format `x, y, z`: "
            )
            lst_input: list[str] = usr_input.split(",")
            assert len(lst_input) == 3  # Check is there is only 3 arguments
            x, y, z = (float(x) for x in lst_input)
            coordinates: tuple[float, float, float] = (x, y, z)
            print(f"Entered cooridnates = {coordinates}")
            return coordinates

        except AssertionError:
            print("Error: exactly 3 coordinates needed, coma separated.")
        except Exception as e:
            print(f"Invalid syntax. Error : {e}")


def calculate_distance(
    crd_1: tuple[float, float, float], crd_2: tuple[float, float, float]
) -> float:
    """
    Calculates distances between two 3D coordinates.
    Algorithm used : Euclidean distance formula

    Args:
        crd_1 (tuple): Position 1
        crd_2 (tuple): Position 2

    Returns:
        float: Distance
    """
    x1, y1, z1 = crd_1
    x2, y2, z2 = crd_2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    """
    Main function
    """
    print("=== Game Coordinate System ===")
    center_coordinates: tuple[float, float, float] = (0.0, 0.0, 0.0)

    print("Get a first set of coordinates")
    set_1: tuple[float, float, float] = get_player_pos()

    distance_1: float = calculate_distance(center_coordinates, set_1)
    print(
        f"Distance to center: {distance_1:.4f}"
    )  # 4 digit floating precision

    print("Get a second set of coordinates")
    set_2: tuple[float, float, float] = get_player_pos()

    distance_2: float = calculate_distance(set_1, set_2)
    print(f"Distance between set_1 and set_2: {distance_2:.4f}")


if __name__ == "__main__":
    main()
