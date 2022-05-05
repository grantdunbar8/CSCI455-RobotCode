from tkinter import *
from tkinter.ttk import *
import _thread, threading
from PIL import ImageTk, Image

master = Tk()
img = None

class UI:
    def __init__(self):
        print("init: UI")
        
    def CreateUI(self):
        print("HERE")

        master.geometry("400x400")

        global img
        img = ImageTk.PhotoImage(Image.open("face1.png"))
        canvas.create_image(20,20, anchor=NW, image=img)

    def OtherMethod(self):
        for i in range(0, 10):
            print(i)
        
class ChangeUI:
    def __init__(self):
        print("init: ChangeUI")
        
    def ChangeImage(self, fileName):
        global img
        img = ImageTk.PhotoImage(Image.open(fileName))
        canvas.create_image(20,20, anchor=NW, image=img)

canvas = Canvas(master, width=300, height=300)
canvas.pack()

inst = UI()

try:
    _thread.start_new_thread(inst.CreateUI,())
    _thread.start_new_thread(inst.OtherMethod,())
except:
    print("ERROR: failed to start thread")

master.mainloop()
