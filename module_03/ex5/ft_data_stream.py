#! /usr/bin/python3
from typing import Generator
import random

"""
Note on typing Generator Functions

https://www.youtube.com/watch?v=DTegfCNAXoM
Generator[YieldType, SendType, ReturnType]

def fn_gen() -> Generator[YieldType, SendType, ReturnType]:

"""


def gen_event(
    names: list[str], actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(
    list_to_consume: list[tuple[str, str]],
) -> Generator[list[tuple[str, str]], None, None]:
    
    while True:
        to_remove = random.choice(list_to_consume)
        print(f"Got event from list : {to_remove}")
        list_to_consume.remove(to_remove)
        yield list_to_consume



def main() -> None:
    """
    Main function
    """
    list_names: list[str] = [
        "alice",
        "bob",
        "charlie",
        "dylan",
        "elon",
        "fabien",
        "gerald",
        "hector",
    ]
    list_action: list[str] = [
        "eat",
        "run",
        "jump",
        "scream",
        "double-jump",
        "bakflip",
        "fly",
        "fight",
    ]

    gen: Generator[tuple[str, str], None, None] = gen_event(
        list_names, list_action
    )

    # Print 1000 times the generator
    # for i in range(1000):
    #     player, action = next(gen)
    #     print(f"Event {i}: Player {player} did action {action}")
    print("===========")

    # Store 10 times the generator
    list_tuples = [next(gen) for x in range(10)]
    print(f"Generated list of 10 events {list_tuples}")

    cms = consume_event(list_tuples)
    for x in range(len(list_tuples)):
        next(cms)
        print(f"Remaining of list : {list_tuples}")



if __name__ == "__main__":
    main()
