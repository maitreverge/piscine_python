from . import dark_spellbook


def validate_ingredients(ingredients: str) -> tuple[str, str]:
    list_ingredient: list[str] = ingredients.split(" ")
    allowed_ingredient: list[str] = (
        dark_spellbook.dark_spell_allowed_ingredients()
    )
    for ingredient in list_ingredient:
        if ingredient.lower() in allowed_ingredient:
            return ("VALID", ingredient)

    return ("INVALID", "")
