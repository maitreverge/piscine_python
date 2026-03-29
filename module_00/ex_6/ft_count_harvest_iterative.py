def ft_count_harvest_iterative() -> None:
    """
    Count and prints from 1 to a given number in iterative.
    """
    days_until_harvest: int = int(input("Days until harvest: "))

    for days in range(1, days_until_harvest + 1):
        print(f"Day {days}")
    print("Harvest time!")
