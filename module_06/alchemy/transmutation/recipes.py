# Absolute import
from elements import create_fire

# Relative import
from ..elements import create_air

# Relative import
from ..potions import strength_potion


def lead_to_gold() -> str:
    ss: str = f"Recipe transmuting Lead toGold: brew `{create_air()}`"
    return f"{ss} and `{strength_potion()}` mixed with `{create_fire()}`"
