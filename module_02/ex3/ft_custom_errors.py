#! /usr/bin/python3


class GardenError(Exception):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)
        self._message = "Unknown garden error" if message is None else message

    def __str__(self) -> str:
        return f"Garden Error: {self._message}"


class PlantError(GardenError):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"PlantError: {self._message}"


class WaterError(GardenError):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"WaterError: {self._message}"


def raise_garden_error(error_message: str | None = None) -> None:
    raise GardenError(error_message)


def raise_plant_error(error_message: str | None = None) -> None:
    raise PlantError(error_message)


def raise_water_error(error_message: str | None = None) -> None:
    raise WaterError(error_message)


def main() -> None:
    """
    Main function
    """

    # Raise and catch GardenError
    try:
        raise_garden_error("The tomato is talking to me.")
    except GardenError as e:
        print(f"{e}")

    # Raise and catch PlantError
    try:
        raise_plant_error("The plant is thirsty.")
    except PlantError as e:
        print(f"{e}")

    # Raise and catch WaterError
    try:
        raise_water_error("The plant is overwatered.")
    except WaterError as e:
        print(f"{e}")

    # Raise and catch an empty error message
    try:
        raise_garden_error()
    except GardenError as e:
        print(f"{e}")

    """
    Prove that catching a GardenError will also catch
    a PlantError and a WaterError, since they are subclasses of GardenError.
    """
    try:
        raise_water_error("Water is not clean.")
    except GardenError as e:
        print(f"{e}")

    try:
        raise_plant_error("The plant is wilting.")
    except GardenError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
