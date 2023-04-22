def speak(text):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()