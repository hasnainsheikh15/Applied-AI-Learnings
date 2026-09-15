import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


class Job(BaseModel):
    title: str
    company: str
    location: str
    skills: list[str]
    experience: str


job_description = """
We are hiring a Junior Backend Engineer at TechNova.

Location: Bangalore, India.

The candidate should have experience with Python, FastAPI,
PostgreSQL and Docker.

This is a 0-2 years experience position.
"""


response = client.responses.parse(
    model="openai/gpt-oss-20b",
    input=job_description,
    text_format=Job
)

job = response.output_parsed

print(job)
print()
print("Title:", job.title)
print("Company:", job.company)
print("Location:", job.location)
print("Skills:", job.skills)
print("Experience:", job.experience)