def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    Prints out inventory differently depending on input.

    Args:
        seed_type (str): Seed type.
        quantity (int): Quantity of seeds.
        unit (str): Unit (`packets`, `grams`, `area`)
    """
    ending_string: str = ""

    match unit:
        case "packets":
            ending_string = f"{quantity} {unit} available"
        case "grams":
            ending_string = f"{quantity} {unit} total"
        case "area":
            ending_string = f"covers {quantity} square meters"
        case _:
            print("Unknown unit type")
            return

    print(f"{seed_type.capitalize()} seeds: {ending_string}")
