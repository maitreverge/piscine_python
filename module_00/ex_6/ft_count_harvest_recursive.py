def ft_count_harvest_recursive() -> None:
    """
    Count and prints from 1 to a given number in recursive.
    """
    days_until_harvest: int = int(input("Days until harvest: "))

    def walk(start: int) -> None:
        if days_until_harvest > start:
            print("Harvest time!")
            return
        print(f"Day {start}")
        walk(start + 1)

    walk(1)
