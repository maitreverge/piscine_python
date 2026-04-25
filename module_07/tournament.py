#! /usr/bin/python3
"""Main for ex03."""

from ex0 import AquaFactory, FlameFactory
from ex0.create_factory import CreatureFactory
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import AgressiveStrategy, DefensiveStrategy, NormalStrategy
from ex2.battle_strategy import BattleStrategy


def factory_name(factory: CreatureFactory) -> str:
    """Return a short, readable name for a creature factory."""
    return factory.__class__.__name__.removesuffix("Factory")


def run_action(creature: Creature, strategy: BattleStrategy) -> str:
    """Run strategy action once and return a printable outcome."""
    try:
        return strategy.act(creature)
    except TypeError as exc:
        return f"Error: {exc}"


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]], nb_match: int
) -> None:
    """Run one tournament between all configured opponents."""
    print(f"Tournament {nb_match}")
    print("[ ", end="")
    for factory, strategy in opponents:
        print(
            f"({factory_name(factory)}+{strategy.__class__.__name__}) ", end=""
        )
    print("]")

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for index, (factory, strategy) in enumerate(opponents, start=1):
        base_creature = factory.create_base()
        evolved_creature = factory.create_evolved()

        print(
            f"Opponent {index}: {factory_name(factory)} + {strategy.__class__.__name__}"
        )
        print(
            f"- Base: {base_creature.name} -> {run_action(base_creature, strategy)}"
        )
        print(
            f"- Evolved: {evolved_creature.name} -> {run_action(evolved_creature, strategy)}"
        )
        print()

    print("-" * 42)
    print()


def main() -> None:
    """Main function."""
    flame_fct = FlameFactory()
    aqua_fct = AquaFactory()
    healing_fct = HealingCreatureFactory()
    transform_fct = TransformCreatureFactory()

    normal_stg = NormalStrategy()
    agressive_stg = AgressiveStrategy()
    defensive_stg = DefensiveStrategy()

    matchmaking = [
        [
            (flame_fct, normal_stg),
            (healing_fct, defensive_stg),
        ],
        [
            (transform_fct, agressive_stg),
            (aqua_fct, normal_stg),
        ],
        [
            (flame_fct, agressive_stg),
            (healing_fct, agressive_stg),
            (transform_fct, defensive_stg),
        ],
    ]

    for match_nb, opponents in enumerate(matchmaking, start=1):
        battle(opponents, match_nb)


if __name__ == "__main__":
    main()
