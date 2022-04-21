from cProfile import label
from cgi import test
from hashlib import shake_128
from multiprocessing.sharedctypes import Value
import kivy
kivy.require('1.0.6')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.label import Label


robotMoveVar1 = ''

def on_slider_val(self, instance, val):
        self.label.text = str(val)


KV = '''
BoxLayout:
    Slider:
        id: s1
    Label:
        text: str(s1.value)
'''


slider = Slider(
    min = 0, 
    max = 10, 
    orientation = 'horizontal',
    value_track = True,
    value_track_color = [1, 0, 0, 1],
    step = 1
    
    )
# slider = Slider(...)
# label1 = Label(...)
label1 = Label()
popupButton = Button(text = "Set Value")


testVal = ''
def OnSliderValueChange(instance,value):
    label1.text = str(value) + " seconds"
    testVal = value
    print(value)
    print("HERE " + str(testVal))
    return value


# def SetLabelTime(instance, value):
#     robotMoveVar1 = str(value)
    



slider.bind(value=OnSliderValueChange)





# sliderVal = NumericProperty(0)
# slider.fbind('value', on_slider_val)
# label24 = Label(text = str(sliderVal))

box = BoxLayout()
box.add_widget(slider)
box.add_widget(label1)
box.add_widget(popupButton)

popup = Popup(title = "ROBOT MOVE WINDOW", content = box, size_hint = (None, None), size = (400, 100))
popupButton.bind(on_press = popup.dismiss)



def makeDropDown(dropdown):
        for i in range(7):
            if i == 0:       
                ddButton = Button(text = "Robot Move", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                ddButton.bind(on_release = popup.open)
                dropdown.add_widget(ddButton)
            elif i == 1:
                ddButton = Button(text = "Robot Turn", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)
            elif i == 2:
                ddButton = Button(text = "Head Tilt", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)
            elif i == 3:
                ddButton = Button(text = "Head Pan", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)
            elif i == 4:
                ddButton = Button(text = "Waist Turn", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)
            elif i == 5:
                ddButton = Button(text = "Human Talk", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)
            elif i == 6:
                ddButton = Button(text = "Robot Talk", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)



class MyApp(App):

    


    def build(self):



        self.window = GridLayout(
            spacing = 10,
            padding = [20, 50, 20, 50],
            ) 
        
            
        self.window.cols = 2
        self.window.rows = 5
        Window.size = (800, 480)

        # dropdown1 = DropDown()
        # dropdown2 = DropDown()
        # dropdown3 = DropDown()
        # dropdown4 = DropDown()
        # dropdown5 = DropDown()
        # dropdown6 = DropDown()
        # dropdown7 = DropDown()
        # dropdown8 = DropDown()

        # ddButton1 = Button(text = "Robot Move", size_hint_y = None)
        # ddButton1.bind(on_release = lambda ddButton1: dropdown1.select(ddButton1.text))
        # #ddButton1.bind(on_release = lambda ddButton1: dropdown2.select(ddButton1.text))

        # ddButton2 = Button(text = "Robot Turn", size_hint_y = None)
        # ddButton2.bind(on_release = lambda ddButton2: dropdown1.select(ddButton2.text))
        # #ddButton2.bind(on_release = lambda ddButton2: dropdown2.select(ddButton2.text))

        # ddButton3 = Button(text = "Head Tilt", size_hint_y = None)
        # ddButton4 = Button(text = "Head Pan", size_hint_y = None)
        # ddButton5 = Button(text = "Waist Turn", size_hint_y = None)
        # ddButton6 = Button(text = "Human Talk", size_hint_y = None)
        # ddButton7 = Button(text = "Robot Talk", size_hint_y = None)

        # dropdown1.add_widget(ddButton1)
        # dropdown1.add_widget(ddButton2)
        # dropdown2.add_widget(ddButton1)
        # dropdown2.add_widget(ddButton2)

        #dropdown2.add_widget(ddButton2)
        dropdown = DropDown()
        dropdown2 = DropDown()
        dropdown3 = DropDown()
        dropdown4 = DropDown()
        dropdown5 = DropDown()
        dropdown6 = DropDown()
        dropdown7 = DropDown()
        dropdown8 = DropDown()


        makeDropDown(dropdown)
        makeDropDown(dropdown2)
        makeDropDown(dropdown3)
        makeDropDown(dropdown4)
        makeDropDown(dropdown5)
        makeDropDown(dropdown6)
        makeDropDown(dropdown7)
        makeDropDown(dropdown8)



        self.button1 = Button(text = "Action 1")
        self.button1.bind(on_release=dropdown.open)
        self.button2 = Button(text = "Action 2")
        self.button2.bind(on_release=dropdown2.open)
        self.button3 = Button(text = "Action 3")
        self.button3.bind(on_release=dropdown3.open)
        self.button4 = Button(text = "Action 4")
        self.button4.bind(on_release=dropdown4.open)
        self.button5 = Button(text = "Action 5")
        self.button5.bind(on_release=dropdown5.open)
        self.button6 = Button(text = "Action 6")
        self.button6.bind(on_release=dropdown6.open)
        self.button7 = Button(text = "Action 7")
        self.button7.bind(on_release=dropdown7.open)
        self.button8 = Button(text = "Action 8")
        self.button8.bind(on_release=dropdown8.open)


        dropdown.bind(on_select=lambda instance, x: setattr(self.button1, 'text', "Action1: " + x + " for: " + str(testVal)))
        dropdown2.bind(on_select=lambda instance, x: setattr(self.button2, 'text', "Action2: " +x))
        dropdown3.bind(on_select=lambda instance, x: setattr(self.button3, 'text', "Action3: " +x))
        dropdown4.bind(on_select=lambda instance, x: setattr(self.button4, 'text', "Action4: " +x))
        dropdown5.bind(on_select=lambda instance, x: setattr(self.button5, 'text', "Action5: " +x))
        dropdown6.bind(on_select=lambda instance, x: setattr(self.button6, 'text', "Action6: " +x))
        dropdown7.bind(on_select=lambda instance, x: setattr(self.button7, 'text', "Action7: " +x))
        dropdown8.bind(on_select=lambda instance, x: setattr(self.button8, 'text', "Action8: " +x))

        #dropdown2.bind(on_select=lambda instance, x: setattr(self.button2, 'text', x))



        red = [1, 0, 0, 1] 
        green = [0, 1, 0, 1] 
        blue = [0, 0.5, 1, 1] 
        purple = [1, 0, 1, 1] 

        self.button9 = Button(
            text = "RUN",
            size_hint_x = None,
            size_hint_y = None,
            width = 100,
            height = 50,
            pos_hint = {"center_x":0.3},
            background_color = blue
            )
        self.button10 = Button(
            text = "EXIT",
            size_hint_x = None,
            size_hint_y = None,
            width = 100,
            height = 50,
            background_color = red
            )





        self.window.add_widget(self.button1)
        self.window.add_widget(self.button2)
        self.window.add_widget(self.button3)
        self.window.add_widget(self.button4)
        self.window.add_widget(self.button5)
        self.window.add_widget(self.button6)
        self.window.add_widget(self.button7)
        self.window.add_widget(self.button8)
        self.window.add_widget(self.button9)
        self.window.add_widget(self.button10)

        return self.window


if __name__ == '__main__':
    MyApp().run()