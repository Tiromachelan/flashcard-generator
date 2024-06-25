# Produces produces flashcards in the form of Question: Answer:

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

def generate_text(filename):
    load_dotenv()

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    with open(filename, "r", encoding="utf-8", errors="ignore") as file:
        user_input = file.read()

    with open("config.json", "r") as config:
        data = json.load(config)


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f'{"You are a flashcard generator that takes text input and produces"}{data["number_of_cards"]}{"concise flashcards based on the text in the form of Question: Answer:"}'},
            {"role": "user", "content": user_input}
        ]
    )

    print(completion.choices[0].message.content)
