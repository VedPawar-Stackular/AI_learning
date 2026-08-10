import pydantic
import json
from app import get_recipe, prompt as recipe_prompt
from models import Recipe
import pytest
from unittest.mock import patch, MagicMock

def test_get_recipe_returns_valid_object():
    fake_recipe = MagicMock()

    fake_recipe.choices[0].message.content = json.dumps({
        "name": "Recipe", 
        "ingredients": ["Ingredient1", "Ingredient2"], "time_minutes": 30
    })

    with patch("app.client.chat.completions.create", return_value=fake_recipe):
        recipe = get_recipe(recipe_prompt)

    assert recipe is not None
    assert recipe.name == "Recipe"
    assert recipe.ingredients == ["Ingredient1", "Ingredient2"]
    assert recipe.time_minutes == 30


def test_get_recipe_raises_validation_error():
    fake_recipe = MagicMock()
    fake_recipe.choices[0].message.content = "Invalid JSON"

    with patch("app.client.chat.completions.create", return_value=fake_recipe):
        recipe = get_recipe(recipe_prompt)

    assert recipe is None



    