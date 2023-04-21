import os
import openai
from dotenv import load_dotenv
from random import choice
from flask import Flask,Request

SessionPromt = 'Talking to a chatbot'
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

startsequence = "\n Py:"
restartsequence = "\n You:"

def ask(question, chat_log=None):
    prompttext = f'{chat_log}{restartsequence}: {question}{startsequence}'
    responce = openai.Completion.create(model="text-davinci-003",max_tokens=150,top_p=1,frequency_penalty=0.47,presence_penalty=0.21,stop = ["\n"])
    story = responce['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = SessionPromt
    return f'{chat_log}{restartsequence} {question}{startsequence}{answer}'
