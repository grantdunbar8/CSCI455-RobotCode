from gtts import gTTS
import os
import os.path

class TextToSpeech:
    print("CLASS")
    def CreateSound(self, fileName, inputText):
        exists = os.path.exists(fileName)

        if exists == False:
            toSpeak = gTTS(text = inputText)
            toSpeak.save(fileName)
        else:
            print("WARNING: File already exists.")
        
    def PlaySound(self, fileName):
        exists = os.path.exists(fileName)

        if exists == True:
            os.system("mpg123 " + fileName)
            print("GOT HERE 1")
            self.RemoveSound(fileName)
            
        else:
            print("ERROR: File does not exist.")

    def RemoveSound(self, fileName):
        if os.path.exists(fileName) == True:
            os.remove(fileName)
            print("removed file")

    def CreateAndPlay(fileName, inputText):
        toSpeak = gTTS(text = inputText)
        toSpeak.save(fileName)
        os.system("mpg123", fileName)
        os.remove(fileName)
        print("RETURN")
        return True
        print("BAD RETURN")
        
