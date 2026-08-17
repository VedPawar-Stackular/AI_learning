from pydantic import BaseModel, Field


class WeatherInput(BaseModel):
    city: str = Field(..., description="The city to get the weather for")

# class WeatherOutput(BaseModel):
#     current_weather_celcuis: float = Field(..., description="The current weather in Celcius")
#     current_weather_fahrenheit: float = Field(..., description="The current weather in Fahrenheit")

class WikipediaInput(BaseModel):
    query: str = Field(..., description="The query to search for on Wikipedia")

# class WikipediaOutput(BaseModel):
#     source: dict[str, str | None] = Field(..., description="The source of the information")


# class ToolCall(BaseModel):
#     name: str = Field(..., description="The name of the tool")
#     arguments: dict = Field(..., description="The arguments passed to the tool")

# class ToolCalls(BaseModel):
#     tool_calls: List[ToolCall] = Field(..., description="A list of tool calls made by the model")