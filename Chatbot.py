from dotenv import load_dotenv
import openai
import os
import resources
import json

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

Textbased = True
Audiobased = False

# Load the conversation history from a file
conversation_history = []
if os.path.exists("conversation_history.json"):
    with open("conversation_history.json", "r") as f:
        conversation_history = json.load(f)

# Generate a response to a new message
def generate_response(prompt):
    # Get the most recent response from the conversation history
    previous_response = conversation_history[-1]["response"] if conversation_history else ""

    # Generate a new response using the OpenAI API
    chat = openai.Completion.create(
        engine="text-curie-001",
        prompt=previous_response + "" +prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )

    response = chat.choices.message["content"].strip()
    # Store the message and response in the conversation history
    #response = chat.choices[-1].text.strip()
    conversation_history.append({"message": prompt, "response": response})
    with open("conversation_history.json", "w") as f:
        json.dump(conversation_history, f)
    

    return response

while Textbased:
    user_input = input('You: ')
    if user_input.lower() == "voice":
        Textbased = False
        Audiobased = True
    else:
        response = generate_response(user_input)
        print("Bot:", response)

while Audiobased:
    user_input = resources.mic_loop()
    if user_input.lower() == "text":
        Textbased = True
        Audiobased = False
    else:
        response = generate_response(user_input)
        resources.speak(response)