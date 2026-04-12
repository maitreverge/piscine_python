from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate, _ = validate_ingredients(ingredients)
    if validate == "VALID":
        return f"Spell {spell_name} is recorded. Ingredient = {ingredients}"

    return f"Spell {spell_name} is rejected. Ingredient = {ingredients}"
