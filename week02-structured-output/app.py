import openai
import pydantic
from config import groq_api_key
from models import Recipe
import json


client = openai.OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

system_prompt = "You are a chef with 25+ years of experience. You must guide the users/your students in whatever recipe they ask you for. You must always give the recipe's name, ingredients, and time in minutes. The user will mention below the recipe they want to learn about. respond only with JSON matching this schema: {'name': 'Recipe', 'schema': Recipe.model_json_schema()}"
user_prompt = "Paneer Butter Masala"

prompt = system_prompt + "\n" + user_prompt

def get_recipe(prompt: str) -> Recipe | None:
    max_attempts = 3
    for attempt in range(0, max_attempts):
        try:
            completion = client.chat.completions.create(
                model="openai/gpt-oss-20b", #openai/gpt-oss-20b, openai/gpt-oss-120b
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
                temperature=0.5,
                response_format={
                    "type": "json_schema", # forcing to return a structured output as JSON object
                    "json_schema": {
                        "name": "Recipe",
                        "schema": Recipe.model_json_schema() # Pydantic model schema
                    }
                }
            )
            output = completion.choices[0].message.content #Json string output from the model
            recipe = Recipe.model_validate_json(output)  # raises ValidationError if shape is wrong
            return recipe  # return the validated Recipe object
            # print(output)


        except pydantic.ValidationError as e: 
            # 2. Store the raw exception object in a variable
            # validation_exception = e
            # 3. Extract and store the details as a Python list of dictionaries
            error_list = e.errors()
            # Convert the list of dictionaries directly into a string
            error_string = json.dumps(error_list)

            #update the prompt with the error string
            prompt += f"\nErrors for attempt {attempt+1}: {error_string}"
            print(f"Attempt {attempt+1} failed. Retrying...")
            if attempt == max_attempts - 1:
                print(f"All attempts failed.")

        except openai.APIError as e:
            print(f"Attempt {attempt+1} failed.")
            print(e)
            raise RuntimeError(f"API error occurred after max retries: {e}")
    
if __name__ == "__main__":
    result = get_recipe(prompt)
    print(result)

