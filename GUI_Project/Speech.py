from gtts import gTTS
import os

class TextToSpeech:
    def ConvertTextToSpeech(self,inputText):
        speech = gTTS(text = inputText)
        speech.save("CurrentSpeech.mp3")
        #playsound.playsound("/home/pi/GUI_Project/CurrentSpeech.wav")
        os.system("mpg123 " + "CurrentSpeech.mp3")
        os.remove("CurrentSpeech.mp3")
        print('here')

    #def PlayTextToSpeech(self):
        #p = vlc.MediaPlayer("CurrentSpeech.mp3")
        #p.play()