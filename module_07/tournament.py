#! /usr/bin/python3
"""
_Main for ex03_
"""

from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AgressiveStrategy, DefensiveStrategy
from ex0.create_factory import CreatureFactory
from ex2.battle_strategy import BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]],  nb_match: int) -> None:
    print(f"Tournament {nb_match}")
    print("[ ", end='')
    for opponent, strategy in opponents:
        print(f"({opponent.__class__.__name__.rstrip("Factory")}+{strategy.__class__.__name__}) ", end='')
    print("]")

    print("*** Tournament ***")

    print(f"{len(opponents)} opponents involved\n")

    




def main() -> None:
    """
    Main function
    """
    # Init factories
    flame_fct = FlameFactory()
    aqua_fct = AquaFactory()
    healing_fct = HealingCreatureFactory()
    transform_fct = TransformCreatureFactory()

    # Init strategies
    normal_stg = NormalStrategy()
    agressive_stg = AgressiveStrategy()
    defensive_stg = DefensiveStrategy()

    matchmaking = [
        [(flame_fct, normal_stg), (healing_fct, defensive_stg)], # match 1
        # [(flame_fct, normal_stg), (healing_fct, defensive_stg)], # match 1
        # [(flame_fct, agressive_stg),(healing_fct, defensive_stg)], # match 2
        # [(aqua_fct, normal_stg), (healing_fct, defensive_stg), (transform_fct, agressive_stg)], # match 3
    ]

    for i, matches in enumerate(matchmaking):
        battle(matches, i)






    

if __name__ == "__main__":
    main()