#! /usr/bin/python3
import random


def main() -> None:
    """
    Main function
    """
    print("=== Game Data Alchemist ===")

    raw_names: list[str] = [
        "alice",
        "Bob",
        "charlie",
        "Dylan",
        "elon",
        "fabien",
        "Gerald",
        "Hector",
    ]

    print(f"Initial raw list = {raw_names}")

    capitalized_names = [x.capitalize() for x in raw_names]
    print(f"New list with all names capitalize = {capitalized_names}")

    only_capitalized = [x for x in raw_names if x == x.capitalize()]
    print(f"New list of capitalized names onl = {only_capitalized}")

    dict_capitalized = {x: random.randint(1, 1000) for x in capitalized_names}

    print(f"Created dict = {dict_capitalized}")
    average_dict = sum(dict_capitalized.values()) / len(dict_capitalized)
    print(f"Score average is {average_dict}")

    high_scores = {
        name: score
        for name, score in dict_capitalized.items()
        if score > average_dict
    }
    print(f"High scores : {high_scores}")


if __name__ == "__main__":
    main()
