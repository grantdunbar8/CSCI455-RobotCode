import gTTS
import os
import os.path

class TextToSpeech:
    def CreateSound(fileName, inputText):
        exists = os.path.exists(fileName) == False

        if exists == False:
            toSpeak = gTTS(text = inputText)
            toSpeak.save(fileName)
        else:
            print("WARNING: File already exists.")
        
    def PlaySound(fileName):
        exists = os.path.exists(fileName)

        if exists == True:
            os.system("mpg123 " + fileName)
        else:
            print("ERROR: File does not exist.")

    def CreateAndPlay(fileName, inputText):
        toSpeak = gTTS(text = inputText)
        toSpeak.save(fileName)
        os.system("mpg123", fileName)
        os.remove(fileName)
