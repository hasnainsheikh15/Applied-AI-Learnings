import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
)

def summarize(messages , previous_summary):
   prompt = f"""

Update the conversation summary.

Previous summary : {previous_summary}

New Conversation messages : {messages}

Create a concise summary that preserves important facts,
preferences, decisions, and context from BOTH the previous
summary and the new messages.
"""
   response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=prompt
    )

   return response.output_text

history = []
summary = ""

while True:
    question = input("You : ")

    if question.lower() == "exit":
        break

    history.append({"role": "user", "content": question})

    context = []

    if summary:
       context.append({
          "role" : "system",
          "content" : f"conversation summary : {summary}"
       })

    context.extend(history)

    response = client.responses.create(model="openai/gpt-oss-20b", input=context)

    history.append({"role": "assistant", "content": response.output_text})

    if(len(history) > 10):
        
     old_messages  = history[:-10]

     summary = summarize(old_messages, summary)

     history = history[-10:]

    print("AI : ", response.output_text)
    print("Summary:", summary)
    print("History:", history)
    print("History Length:", len(history))
   
