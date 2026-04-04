#! /usr/bin/python3
import random
import pprint

"""
Set reminder : Immutable, but can add/remove values
Unordered, does not allows duplicates

Syntax : {}
"""


def gen_player_achievements() -> set[str]:
    all_achievements: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        # "First Steps",
        # "Collector Supreme",
        # "Untouchable",
        # "Sharp Mind",
        # "Boss Slayer",
    ]

    rdm_number = random.randint(1, len(all_achievements))

    # * Note : random.sample only accept iterables objects such a lists.
    # * k == number of randomly selected items.
    # * set() constructor has been used because `random.sample` returns a list
    return set(random.sample(all_achievements, k=rdm_number))


def display_stats(persons: dict[str, set[str]]) -> None:
    # for person, achievement in persons.items():
    #     print(f"Player {person.capitalize()}: {achievement}")

    # * Note : `*` operator stands for unpacking
    # `set.union` implies at least one arguments, crashes if dict empty
    # `set().union` creates a emptyset first, so does not crash if dict is empty
    distinct_achievements = set().union(*persons.values())

    print(f"There is {len(distinct_achievements)} distincts achievements")
    print(distinct_achievements)
    print("======")

    all_people_achievements: list[set] = list(persons.values())

    for person, achievement in persons.items():
        # print(f"Only {person.capitalize()} has :", end='')
        print(f"\nCurrent {person.capitalize()} has {len(achievement)} achievement(s) = {achievement}")
        # print(f"All people achivemment : {all_people_achievements}")

        # ! STEP 1 : Track Uniqueness
        # Removed current person's achievement to all people achievement
        cleanned_achievements = [
            x for x in all_people_achievements if achievement != x
        ]

        diff = set(achievement).difference(*cleanned_achievements)
        if diff == set():
            # print(f"Player {person.capitalize()} has no unique achievement")
            print(
                f"\033[31mPlayer {person.capitalize()} has no unique achievement\033[0m"
            )
        else:
            # print(f"")
            print(
                f"\033[32mPlayer {person.capitalize()} has unique achievements = {diff}\033[0m"
            )
        # ! STEP 2 : Track Missing achievements
        missing_achievements = set(distinct_achievements).difference(achievement)

        if missing_achievements == set():
            print(f"\033[32m{person.capitalize()} has all achievements\033[0m")
        else:
            print(f"\033[31m{person.capitalize()} miss {len(missing_achievements)} achievements : {missing_achievements} \033[0m")

    # print(f"All people achievements = {all_people_achievements}")
    # ! Find achievements shared by the players
    intersection = set.intersection(*all_people_achievements)

    # ! Important : `set().intersection` will always compare null with something else,
    # ! which will ultimately return null.
    # intersection_parenthesis = set().intersection(*all_people_achievements)
    if intersection == set():
        print(f"\n\033[31mThere is no common achievements\033[0m")
    else:
        print(f"\n\033[32mCommon achievements = {intersection}\033[0m")


def main() -> None:
    """
    Main function
    """
    print("=== Achievement Tracker System ===")

    persons: dict[str, set] = {
        "alice": gen_player_achievements(),
        "bob": gen_player_achievements(),
        "chalie": gen_player_achievements(),
        "dylan": gen_player_achievements(),
    }

    display_stats(persons)


if __name__ == "__main__":
    main()
