import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

print(f"API_KEY: {api_key}")
print(f"BASE_URL: {base_url}")

try:
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    completion = client.chat.completions.create(
        model="qwen-turbo", # Use a standard model name just in case
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
