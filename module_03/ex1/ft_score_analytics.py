#! /usr/bin/python3
import sys


def display_values(my_list: list[int]) -> None:
    print(f"Score processed: {my_list}")
    print(f"Total players: {len(my_list)}")
    print(f"Total Score: {sum(my_list)}")
    print(
        f"Average score: {sum(my_list) / len(my_list):.1f}"
    )  # 1 digit precision
    print(f"High score: {max(my_list)}")
    print(f"Low score: {min(my_list)}")
    print(f"Score range: {max(my_list) - min(my_list)}")


def main() -> None:
    """
    Main function
    """
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    nb_list: list[int] = []

    for arg in sys.argv[1:]:
        try:
            value_i = int(arg)
            nb_list.append(value_i)
        except Exception as e:
            print(f"Non int value {arg}. Error raised : {e}")

    display_values(nb_list)


if __name__ == "__main__":
    main()
