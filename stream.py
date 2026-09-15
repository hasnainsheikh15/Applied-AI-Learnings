import os
import time
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

start = time.time()

stream = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Explain what an API is in simple terms.",
    stream=True
)

for event in stream:
    if event.type == "response.output_text.delta":
        print( f"\n[{time.time() - start:.3f}s] "
            f"{repr(event.delta)}",
            flush=True)
