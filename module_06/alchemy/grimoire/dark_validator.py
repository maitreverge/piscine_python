from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> tuple[str, str]:
    list_ingredient: list[str] = ingredients.split(" ")
    allowed_ingredient: list[str] = dark_spell_allowed_ingredients()
    for ingredient in list_ingredient:
        if ingredient.lower() in allowed_ingredient:
            return ("VALID", ingredient)

    return ("INVALID", "")
