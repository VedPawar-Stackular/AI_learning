from config import groq_api_key
import openai
from tools import get_weather, search_wikipedia
from models import ToolCall, ToolCalls, WeatherInput, WeatherOutput, WikipediaInput, WikipediaOutput
import json

client = openai.OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

# Tool schema
tools = [
    openai.pydantic_function_tool(
        model=WeatherInput,
        name="get_weather",
        description="Get the current weather for a given city. Takes a city/country/region name as input and returns the current weather in Celcius and Fahrenheit for that city.",
    ),
    openai.pydantic_function_tool(
        model=WikipediaInput,
        name="search_wikipedia",
        description="Search Wikipedia for a given query. Takes a query string as input and returns a dictionary of search results from Wikipedia.",
    )
]

python_tools = {
    "get_weather": get_weather,
    "search_wikipedia": search_wikipedia
}
pydantic_models = {
    "get_weather": WeatherInput,
    "search_wikipedia": WikipediaInput
}


def main():
    system_prompt = """
    Role: You are a helpful assistant that asnwers users query. 
    Contraints: Never guess facts. You are not allowed to make up facts. 
    Choose only one tool at a time to use.
    Think before you answer: Always think about the answer before you answer.
    """
    user_prompt = """
    User: Give me a wikipidia knowledge about cars?
    """
    prompt = system_prompt + "\n" + user_prompt
    
    # Create a running input list we will add to over time
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools,
        temperature=0.6,
        max_tokens=1000,
        # response_format={
        #    "type": "json_schema",
        #    "json_schema": {
        #        "name": "ToolCalls",
        #        "schema": ToolCalls.model_json_schema(),
        #    },
        # },
        # so the response format is not required for a tool call, but it can be given for the final output of the LLM that is need to be sent to the user. The tool call is a separate step that is not part of the final output, but it is part of the LLM's reasoning process. The LLM can use the tool call to get information from the tool and then use that information to generate a final output that is sent to the user.
    )

    if response.choices[0].message.tool_calls is None:
        output = response.choices[0].message.content
        print(output)
        
    else:
        response_message = response.choices[0].message #this is the message key that contains a dictionary of the LLM's response, including the content and the tool_calls
        messages.append(response_message.model_dump(exclude_none=True))

        tool_calls = response_message.tool_calls

        # 3. Handle the tool execution safely with validation
        if tool_calls:
            for tool_call in tool_calls:
                name = tool_call.function.name
                raw_args = json.loads(tool_call.function.arguments)

                print(f"AI requested tool: {name} with arguments:   {raw_args}") #this is the name of the tool and the arguments passed to the tool

                if name in python_tools:
                    try:
                        # Validate the arguments using Pydantic before  running code
                        validated_data = pydantic_models[name](**raw_args)

                        # Unpack the safe data and run the python function
                        # WeatherInput -> validated_data.city |     WikipediaInput -> validated_data.query
                        result = None
                        if name == "get_weather":
                            result = python_tools[name](validated_data.city)
                        elif name == "search_wikipedia":
                            result = python_tools[name](validated_data.query)

                        # Add the tool result to the input list
                        # tool result can only be a string, not a dict, so we need to convert it to a string
                        messages.append({
                            "role": "tool", 
                            "tool_call_id": tool_call.id, 
                            "name": name, 
                            "content": json.dumps(result) if result is not None else "None"
                        })

                        print(f"Tool Result: {result}")

                        response = client.chat.completions.create(
                            model="openai/gpt-oss-20b",
                            tools=tools,
                            messages=messages,
                            temperature=0.6,
                            max_tokens=1000,
                        )

                        # 5. The model should be able to give a response!
                        print("Final output:")
                        print(response.model_dump_json(indent=2))
                        print("Final output content:")
                        print(response.choices[0].message.content)

                    except Exception as e:
                        print(f"Validation or runtime error: {e}")

if __name__ == "__main__":
    main()  