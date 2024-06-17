# Produces produces flashcards in the form of Question: Answer:

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

with open("user_input.txt", "r", encoding="utf-8", errors="ignore") as file:
    user_input = file.read()


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a flashcard generator that takes text input and produces several concise flashcards based on the text in the form of Question: Answer:"},
        {"role": "user", "content": user_input}
    ]
)

print(completion.choices[0].message.content)