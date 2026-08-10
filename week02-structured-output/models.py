from pydantic import BaseModel, Field

class Recipe(BaseModel):
    name: str = Field(..., description="The recipe's name")
    ingredients: list[str] = Field(..., description="The recipe's ingredients")
    time_minutes: int = Field(..., description="The time it takes to prepare the recipe in minutes")

 