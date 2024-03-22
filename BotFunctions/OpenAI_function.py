from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def answer_prompt(prompt):

    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    response = response.choices[0].message.content

    return response
