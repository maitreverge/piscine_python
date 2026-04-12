from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate, _ = validate_ingredients(ingredients)
    # validate, _ = dark_validator.validate_ingredients(ingredients)
    if validate == "VALID":
        return f"Spell {spell_name} is recorded. Ingredient = {ingredients}"

    return f"Spell {spell_name} is rejected. Ingredient = {ingredients}"
