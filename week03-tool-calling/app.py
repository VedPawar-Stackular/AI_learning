from config import groq_api_key
import openai
from tools import get_weather


client = openai.OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)


tools = [get_weather]

def chatbot(prompt: str) -> str:
    
    

