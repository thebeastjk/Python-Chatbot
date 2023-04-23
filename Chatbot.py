from dotenv import load_dotenv
import openai
import os
import resources


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')



# Load the conversation history from a file

# Generate a response to a new message
def generate_response(prompt):
    # Get the most recent response from the conversation history

    # Generate a new response using the OpenAI API
    chat = openai.Completion.create(
        engine="ada",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )

    response = chat.choices[0].text.strip()
    # Store the message and response in the conversation history
    #response = chat.choices[-1].text.strip()

    return response


Textbased = True
Audiobased = False


def loop(Textbased, Audiobased):

    while Textbased:
        user_input = input('You: ')
        if user_input.lower() == "voice":
            Textbased = False
            Audiobased = True
            loop(Textbased, Audiobased)
        else:
            response = generate_response(user_input)
            print("Bot:", response)

    while Audiobased:
        user_input = resources.mic_loop()
        if user_input.lower() == "text":
            Textbased = True
            Audiobased = False
            loop(Textbased, Audiobased)
        else:
            response = generate_response(user_input)
            resources.speak(response)

loop(Textbased, Audiobased)