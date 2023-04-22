def micrec(r,mic):

    import speech_recognition as sr
    if not isinstance(r, sr.Recognizer):
        raise TypeError("`r` must be `Recognizer` instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("`mic` must be `Microphone` instance")

    with mic as source:
        audio = r.listen(source)

    return r.recognize_google(audio)

def speak(text):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def mic_loop():
    r = sr.Recognizer()
    mic = sr.Microphone()
    import speech_recognition as sr
    try:
        text=micrec(r,mic)
    except sr.RequestError:
        text = ("oh shoot... there was a request error")
    except sr.UnknownValueError:
        text  = ("no idea what you said there man...")
    return(text)

