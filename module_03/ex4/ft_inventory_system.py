#! /usr/bin/python3

import sys


class DuplicateError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


def get_inventory() -> dict[str, int]:
    result: dict[str, int] = dict()

    raw_inventory = sys.argv[1:]

    for raw_arg in raw_inventory:
        try:
            item, str_quantity = raw_arg.split(":")
            assert item.isalpha()
            quantity: int = int(str_quantity)
            assert quantity > 0
            # Check for duplicates
            if item.lower() in result.keys():
                raise DuplicateError(f"{item} is already in the inventory")
            result.update({item.lower(): quantity})
        except Exception as e:
            print(f"Wrong format for argument {raw_arg}. Error : {e}")

    return result


def display_inventory(inventory: dict[str, int]) -> None:
    sum_inventory: int = sum(inventory.values())
    print(f"Current inventory: {inventory}")
    print(f"Inventory's items = {list(inventory.keys())}")
    print(f"There is {sum_inventory} items in the inventory")

    for item, quantity in inventory.items():
        print(
            f"Item {item} represents {(quantity / sum_inventory * 100):.1f}%"
        )

    # I ain't time for reinventing the weel
    min_quantity = min(inventory.values())
    max_quantity = max(inventory.values())

    min_item = [
        item
        for item, quantity in inventory.items()
        if quantity == min_quantity
    ][:1]
    max_item = [
        item
        for item, quantity in inventory.items()
        if quantity == max_quantity
    ][:1]
    print(f"Item least abundant : {min_item} with quantity of {min_quantity}")
    print(f"Item most abundant : {max_item} with quantity of {max_quantity}")

    inventory.update({"mega-sword": 2})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    """
    Main function
    sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
    """
    if len(sys.argv) == 1:
        print("Please enter at least")

    inventory: dict[str, int] = get_inventory()

    if len(inventory) == 0:
        print("Empty inventory. Aborting")
        return

    display_inventory(inventory)


if __name__ == "__main__":
    main()
