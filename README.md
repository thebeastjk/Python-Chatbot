[![Python 3.10.11](https://img.shields.io/badge/python-3.10.11-blue.svg)](https://www.python.org/downloads/release/python-3100/)
# Python-Chatbot
just another python chatbot

## Startup

If you want to use this, just clone the git and create a .env file inside the folder, simply put your openai api key inside the .env file like so:
```
export OPENAI_API_KEY = (your openai api key)
```
Then you can run Chatbot.py through command prompt and it should work!

note: if you type `voice` into the prompt you will switch to voice mode!
This will allow you to talk to the AI, just speak into your microphone and the AI will respond.

## Resources

Resources contains all the logic needed to make the audio work for the AI, some different modules to make it easier to code in voice recognition and speech.
Feel free to use the code there, as it's really just `Speech_Recognition` and `PyTtsx3` put in one file
