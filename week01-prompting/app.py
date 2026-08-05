# a CLI script that sends a prompt(system + user) and returns raw text.

import os
import sys
import openai
from config import groq_api_key


# sys.stdout.reconfigure(encoding="utf-8")

system_prompt = "You are a helpful assistant that answers questions based on the provided context. Be to the point and give concise answers. If you don't know the answer, say 'I don't know'. Do not make up answers. Give straight answers, no sentence fragments."
user_prompt = "What is the capital of France? Give the answer as a news journalist in quotes."

prompt = system_prompt + "\n" + user_prompt

client = openai.OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b", #openai/gpt-oss-20b, openai/gpt-oss-120b
    messages=[{"role": "user", "content": prompt}],
    max_tokens=200,
    temperature=0.5,
)

print(completion.choices[0].message.content)