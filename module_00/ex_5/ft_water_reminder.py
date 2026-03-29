def ft_water_reminder() -> None:
    """
    Useris prompter to enter since when plants were watered.
    Then, print a message depending on the provided number.
    """
    last_watering: int = int(input("Days since last watering: "))

    if last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
