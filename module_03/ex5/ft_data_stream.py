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
    """
    Generate random events with player names and actions.

    Args:
        names (list[str]): _list of player names_
        actions (list[str]): _list of possible actions_

    Yields:
        Generator[tuple[str, str], None, None]: _generator yielding tuples of (player name, action)_
    """
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(
    list_to_consume: list[tuple[str, str]],
) -> Generator[list[tuple[str, str]], None, None]:
    """
    Consume a list of events by randomly removing one event at a time and yielding the remaining list.

    Args:
        list_to_consume (list[tuple[str, str]]): _list of events to consume, where each event is a tuple of (player name, action)_

    Yields:
        Generator[list[tuple[str, str]], None, None]: _generator yielding the remaining list of events after each removal_
    """
    local_list = list(list_to_consume)

    while local_list:
        to_remove = random.choice(local_list)
        print(f"Got event from list : {to_remove}")
        local_list.remove(to_remove)
        # ! Note : Yielding a snapshot prevent accessing the local_list
        # ! outside of this generator function.
        yield list(local_list)


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
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did action {action}")
    print("===========")

    # Store 10 times the generator
    list_tuples = [next(gen) for _ in range(10)]
    print(f"Generated list of 10 events {list_tuples}")

    # Consume them
    consume_gen = consume_event(list_tuples)
    for remaining in consume_gen:
        print(f"Remaining of list : {remaining}")


if __name__ == "__main__":
    main()
