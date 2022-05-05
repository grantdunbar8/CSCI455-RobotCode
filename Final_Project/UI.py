from tkinter import *
from tkinter.ttk import *
import _thread, threading

master = Tk()

class UI:
    def __init__(self):
        print("init")
        
    def CreateUI(self):
        print("HERE")

        master.geometry("200x200")
        label = Label(master, text="Test")
        label.pack(pady=10)

    def OtherMethod(self):
        for i in range(0, 100):
            print(i)
        
inst = UI()

try:
    _thread.start_new_thread(inst.CreateUI,())
    _thread.start_new_thread(inst.OtherMethod,())
except:
    print("ERROR: failed to start thread")

master.mainloop()
