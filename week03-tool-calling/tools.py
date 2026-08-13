import re
import requests
import html


def get_weather(city: str) -> dict: #the input city can be entered wrong by the user, but this city is not the exact value that is taken from the user, it is the value that is passed to the function by the LLM, which may understand the misinput from the user and correct it to a valid city name. The function will then use this corrected city name to fetch the weather data from the API.
    #Open the URL for the weather API

    """
    This function takes a city/country/region name as input and returns the current weather in Celcius and Fahrenheit for that city.
    """
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    
    #Check if the request was successful
    if response.status_code == 200:
        #Parse the JSON response
        data = response.json()
        
        #Extract the current weather from the JSON data
        current_weather_celcuis = data["current_condition"][0]["temp_C"]
        current_weather_fahrenheit = data["current_condition"][0]["temp_F"]
        
        #Return the current weather
        return {
            "city": city,
            "temperature_celsius": current_weather_celcuis,
            "temperature_fahrenheit": current_weather_fahrenheit
        }
    else:
        return {"error": "No weather data found for that city."}


def search_wikipedia(query: str) -> dict | None:
    """
    This function takes a query string as input and returns a dictionary of search results from Wikipedia.
    """
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
    headers = {"User-Agent": "week03-tool-calling-learning-project (your-email-or-github-url)"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        source = {}
        if data["query"]["searchinfo"]["totalhits"] > 0:
            for i in data["query"]["search"]:
                # 1. Convert the \u003C into < and \u003E into >
                clean_html = html.unescape(i["snippet"])
                # 2. Strip out all HTML tags using a regular expression pattern. (This  looks for anything inside < and > brackets and deletes it)
                clean_text = re.sub(r'<[^>]*>', '', clean_html)
                source[i["title"]] = clean_text
            return source

    else:
        print("No results found for that query.")
        return {"error": "No results found for that query."}