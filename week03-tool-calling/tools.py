#Tool calling function to get the current weather for a given city
def get_weather(city: str) -> str: #returning string JSON object with the current weather for a given city
    """
    Get the current weather for a given city that the user asks about.

    Args:
        city (str): The name of the city to get the weather for."""
    prompt = f"Get the current weather for {city} in Celcius and Farenheit."
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.5,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "Weather",
                "schema": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "temperature_in_celcius": {"type": "number"},
                        "temperature_in_farenheit": {"type": "number"},
                        # "pressure": {"type": "number"},
                        # "humidity": {"type": "number"},
                        # "wind_speed": {"type": "number"},
                        # "humidity": {"type": "number"},
                        # "wind_speed": {"type": "number"},
                    },
                },
            }
        }
    )
    if response.choices[0].message.content is None:
        return "No weather data found for that city."
    else:
        return response.choices[0].message.content