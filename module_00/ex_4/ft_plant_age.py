def ft_plant_age() -> None:
    """
    Users enters plant age, and prints out different messages
    depending on plant's age.
    """
    plant_age: int = int(input("Enter plant age in days: "))

    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
