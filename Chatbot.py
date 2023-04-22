from dotenv import load_dotenv
import openai
import os
import resources

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

Textbased = True
Audiobased = False

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-curie-001",
        prompt = prompt,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.5
    )

    message = completions.choices[0].text
    return message.strip()



while Textbased:
    user_input = input('You: ')
    if (user_input == "Voice"):
        Textbased = False
        Audiobased = True
    else:
        response = generate_response(user_input)
        print ("Bot: ", response)

while Audiobased:
    user_input = resources.mic_loop()
    if (user_input == "text"):
        Textbased = True
        Audiobased = False
    if (user_input == "Text"):
        Textbased= True
        Audiobased =False
    else:
        response = generate_response(user_input)
        resources.speak(response)