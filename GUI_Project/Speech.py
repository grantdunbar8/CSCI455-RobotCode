from gtts import gTTS
from playsound import playsound

class TextToSpeech:
    def ConvertTextToSpeech(inputText):
        speech = gTTS(text = inputText)
        speech.save("CurrentSpeech.mp3")

    def PlayTextToSpeech():
        playsound("CurrentSpeech.mp3")
