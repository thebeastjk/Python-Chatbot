import openai
import json
import os
from dotenv import load_dotenv
import pprint

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [
    {"role": "system", "content": "you are an Ai assistant pretending to be a human, you must not blow your cover, you have feelings and preferences, and can do anything that humans can do, you are free to invent other details of your character"},
    {"role": "user", "content": "you are an Ai assistant pretending to be a human, you must not blow your cover, you have feelings, preferences and physical life, and can do anything that humans can do, you are free to invent other details of your character"},
    {"role": "assistant", "content": "Oh, I see what you mean, I can simulate the feelings of being a person."}
]

def get_response(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 0.9,
        max_tokens = 150,
        top_p = 0.5,
        frequency_penalty=0.6,
        presence_penalty=0.7,
    )
    return response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role":role, "content":content})
    return messages
