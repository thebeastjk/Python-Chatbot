from dotenv import load_dotenv
import openai
import os
import resources
from speech import get_response,update_chat
import speech

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


Textbased = True
Audiobased = False


def loop(Textbased, Audiobased):
    messages = speech.messages
    while Textbased:
        user_input = input('You: ')
        if user_input.lower() == "voice":
            Textbased = False
            Audiobased = True
            loop(Textbased, Audiobased)
        if user_input.lower() == "exit":
            break
        else:
            messages = update_chat(messages, "user", user_input)
            modelresponse = get_response(messages)
            messages = update_chat(messages, "assistant", modelresponse)
            print("Bot:", modelresponse)

    while Audiobased:
        user_input = resources.mic_loop()
        if user_input.lower() == "text":
            Textbased = True
            Audiobased = False
            loop(Textbased, Audiobased)
        else:
            messages = update_chat(messages, "user", user_input)
            modelresponse = get_response(messages)
            messages = update_chat(messages, "assistant", modelresponse)
            resources.speak(modelresponse)
speech.__init__(input('Session ID: '))
loop(Textbased, Audiobased)