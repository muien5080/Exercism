"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    # Check if any ingredient is alcohol
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    name, ingredients = dish
    return (name, set(ingredients) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    # Union of all ingredient sets
    result = set()
    for dish in dishes:
        result |= dish
    return result


def separate_appetizers(dishes, appetizers):
    # Remove duplicates and subtract
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    # All ingredients minus shared ones
    all_ingredients = set()
    for dish in dishes:
        all_ingredients |= dish

    return all_ingredients - intersection