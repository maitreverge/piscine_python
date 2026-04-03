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


def water_plant(plant_name: str) -> None:
    print(f"[Attempt to water {plant_name}]")

    if plant_name != plant_name.capitalize():
        raise PlantError("Plant name is not capitalized.")


def main() -> None:
    """
    Main function
    """
    print("=== Garden Watering System ===")

    plant_names: list[str] = ["Tomato", "letuce", "cUcUmber", "OAk"]

    for plant in plant_names:
        try:
            water_plant(plant)
        except PlantError:
            print("Provided argument is not a string")
        else:
            print(f"{plant} successfully watered")
        finally:
            print("=== Closing the watering system ===")

    print("cleanup always happens, even when there’s an error")


if __name__ == "__main__":
    main()
