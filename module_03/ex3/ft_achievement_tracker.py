#! /usr/bin/python3
import random
import pprint

"""
Set reminder : Immutable, but can add/remove values
Unordered, does not allows duplicates

Syntax : {}
"""


def gen_player_achievements() -> set[str]:
    all_achivements: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        # "Survivor",
        # "Master Explorer",
        # "Treasure Hunter",
        # "Unstoppable",
        # "First Steps",
        # "Collector Supreme",
        # "Untouchable",
        # "Sharp Mind",
        # "Boss Slayer",
    ]

    rdm_number = random.randint(1, len(all_achivements))

    # * Note : random.sample only accept iterables objects such a lists.
    # * k == number of randomly selected items.
    # * set() constructor has been used because `random.sample` returns a list
    return set(random.sample(all_achivements, k=rdm_number))

def display_stats(persons: dict[str, set[str]]) -> None:
    # for person, achivement in persons.items():
    #     print(f"Player {person.capitalize()}: {achivement}")

    # * Note : `*` operator stands for unpacking
    # `set.union` implies at least one arguments, crashes if dict empty
    # `set().union` creates a emptyset first, so does not crash if dict is empty
    distinct_achivements = set().union(*persons.values())
    
    print(f"There is {len(distinct_achivements)} distincts achivements")
    print(distinct_achivements)
    print("======")

    all_people_achivements: list[set] = list(persons.values())
    
    # Uniqueness
    for person, achivement in persons.items():
        # print(f"Only {person.capitalize()} has :", end='')
        print(f"Current {person.capitalize()} achivement = {achivement}\n")
        # print(f"All people achivemment : {all_people_achivements}")
        
        # Removed current achivements to all people achivement
        cleanned_achivements = [x for x in all_people_achivements if achivement != x]
        # print(f"Cleanned = {cleanned_achivements}")
        
        diff = set(achivement).difference(*cleanned_achivements)
        
        if diff ==set():
            print(f"Player {person.capitalize()} has no unique achivement")
        else:
            print(f"Player {person.capitalize()} has unique achivements = {diff}")

    
    

    


def main() -> None:
    """
    Main function
    """
    print("=== Achievement Tracker System ===")

    persons: dict[str, set] = {
        # "alice": gen_player_achievements(),
        "alice": {"test1", "test2"},
        "bob": gen_player_achievements(),
        "chalie": gen_player_achievements(),
        "dylan": gen_player_achievements(),
    }

    display_stats(persons)

if __name__ == "__main__":
    main()
