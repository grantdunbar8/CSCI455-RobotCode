
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


# def on_slider_val(self, instance, val):
#         self.label.text = str(val)

    
KV = '''
BoxLayout:
    Slider:
        id: s1
    Label:
        text: str(s1.value)
'''


class MyApp(App):

    def makeDropDown(self, dropdown, popup, popup2):
        for i in range(7):
            if i == 0:       
                ddButton = Button(text = "Robot Move", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                ddButton.bind(on_release = popup.open)
                dropdown.add_widget(ddButton)
            elif i == 1:
                ddButton = Button(text = "Robot Turn", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                ddButton.bind(on_release = popup2.open)
                dropdown.add_widget(ddButton)
            elif i == 2:
                ddButton = Button(text = "Head Tilt", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                ddButton.bind(on_release = popup2.open)
                dropdown.add_widget(ddButton)
            elif i == 3:
                ddButton = Button(text = "Head Pan", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                ddButton.bind(on_release = popup2.open)
                dropdown.add_widget(ddButton)
            elif i == 4:
                ddButton = Button(text = "Waist Turn", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                ddButton.bind(on_release = popup2.open)
                dropdown.add_widget(ddButton)
            elif i == 5:
                ddButton = Button(text = "Human Talk", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)
            elif i == 6:
                ddButton = Button(text = "Robot Talk", size_hint_y = None)
                ddButton.bind(on_release = lambda ddButton: dropdown.select(ddButton.text))
                dropdown.add_widget(ddButton)


    ############make update only update the button you want to - good I think
    def update(self, event):

        if ('Action1' in self.button1.text):
            if ('seconds' not in self.button1.text) and ('Robot Move' in self.button1.text):
                newText = self.button1.text + " for: " + str(self.testVal) + " seconds"
                self.button1.text = newText
            elif ('plus' not in self.button1.text) and (('Robot Turn' in self.button1.text) or ('Head Tilt' in self.button1.text) or ('Head Pan' in self.button1.text) or ('Waist Turn' in self.button1.text)):
                newText = self.button1.text + " plus: " + str(self.testVal)
                self.button1.text = newText

        if ('Action2' in self.button2.text):
            if ('seconds' not in self.button2.text) and ('Robot Move' in self.button2.text):
                newText = self.button2.text + " for: " + str(self.testVal) + " seconds"
                self.button2.text = newText
            elif ('plus' not in self.button2.text) and (('Robot Turn' in self.button2.text) or ('Head Tilt' in self.button2.text) or ('Head Pan' in self.button2.text) or ('Waist Turn' in self.button2.text)):
                newText = self.button2.text + " plus: " + str(self.testVal)
                self.button2.text = newText

        if ('Action3' in self.button3.text):
            if ('seconds' not in self.button3.text) and ('Robot Move' in self.button3.text):
                newText = self.button3.text + " for: " + str(self.testVal) + " seconds"
                self.button3.text = newText
            elif ('plus' not in self.button3.text) and (('Robot Turn' in self.button3.text) or ('Head Tilt' in self.button3.text) or ('Head Pan' in self.button3.text) or ('Waist Turn' in self.button3.text)):
                newText = self.button3.text + " plus: " + str(self.testVal)
                self.button3.text = newText

        if ('Action4' in self.button4.text):
            if ('seconds' not in self.button4.text) and ('Robot Move' in self.button4.text):
                newText = self.button4.text + " for: " + str(self.testVal) + " seconds"
                self.button4.text = newText
            elif ('plus' not in self.button4.text) and (('Robot Turn' in self.button4.text) or ('Head Tilt' in self.button4.text) or ('Head Pan' in self.button4.text) or ('Waist Turn' in self.button4.text)):
                newText = self.button4.text + " plus: " + str(self.testVal)
                self.button4.text = newText

        if ('Action5' in self.button5.text):
            if ('seconds' not in self.button5.text) and ('Robot Move' in self.button5.text):
                newText = self.button5.text + " for: " + str(self.testVal) + " seconds"
                self.button5.text = newText
            elif ('plus' not in self.button5.text) and (('Robot Turn' in self.button5.text) or ('Head Tilt' in self.button5.text) or ('Head Pan' in self.button5.text) or ('Waist Turn' in self.button5.text)):
                newText = self.button5.text + " plus: " + str(self.testVal)
                self.button5.text = newText

        if ('Action6' in self.button6.text):
            if ('seconds' not in self.button6.text) and ('Robot Move' in self.button6.text):
                newText = self.button6.text + " for: " + str(self.testVal) + " seconds"
                self.button6.text = newText
            elif ('plus' not in self.button6.text) and (('Robot Turn' in self.button6.text) or ('Head Tilt' in self.button6.text) or ('Head Pan' in self.button6.text) or ('Waist Turn' in self.button6.text)):
                newText = self.button6.text + " plus: " + str(self.testVal)
                self.button6.text = newText

        if ('Action7' in self.button7.text):
            if ('seconds' not in self.button7.text) and ('Robot Move' in self.button7.text):
                newText = self.button7.text + " for: " + str(self.testVal) + " seconds"
                self.button7.text = newText
            elif ('plus' not in self.button7.text) and (('Robot Turn' in self.button7.text) or ('Head Tilt' in self.button7.text) or ('Head Pan' in self.button7.text) or ('Waist Turn' in self.button7.text)):
                newText = self.button7.text + " plus: " + str(self.testVal)
                self.button7.text = newText

        if ('Action8' in self.button8.text):
            if ('seconds' not in self.button8.text) and ('Robot Move' in self.button8.text):
                newText = self.button8.text + " for: " + str(self.testVal) + " seconds"
                self.button8.text = newText
            elif ('plus' not in self.button8.text) and (('Robot Turn' in self.button8.text) or ('Head Tilt' in self.button8.text) or ('Head Pan' in self.button8.text) or ('Waist Turn' in self.button8.text)):
                newText = self.button8.text + " plus: " + str(self.testVal)
                self.button8.text = newText


    def build(self):

        self.window = GridLayout(
            spacing = 10,
            padding = [20, 50, 20, 50],
            ) 
        
            
        self.window.cols = 2
        self.window.rows = 5
        Window.size = (800, 480)

        dropdown = DropDown()
        dropdown2 = DropDown()
        dropdown3 = DropDown()
        dropdown4 = DropDown()
        dropdown5 = DropDown()
        dropdown6 = DropDown()
        dropdown7 = DropDown()
        dropdown8 = DropDown()

        self.testVal = ''


        def OnSliderValueChange(instance, value):
            label1.text = str(value) + " seconds"
            self.testVal = value
            # print(value)
            # print("HERE " + str(self.testVal))
            # print(instance)
            #return value

        slider = Slider(
            min = -10, 
            max = 10, 
            orientation = 'horizontal',
            value_track = True,
            value_track_color = [1, 0, 0, 1],
            step = 1
            
            )
       
        label1 = Label()
        popupButton = Button(text = "Set Value")
        slider.bind(value=OnSliderValueChange)
        box = BoxLayout()
        box.add_widget(slider)
        box.add_widget(label1)
        box.add_widget(popupButton)
        popup = Popup(title = "+ = forward | - = backward", content = box, size_hint = (None, None), size = (400, 100))
        popupButton.bind(on_press = popup.dismiss)
        popupButton.bind(on_press = self.update)

#################################################
        def OnSliderValueChange2(instance, value):
            label2.text = str(value) 
            self.testVal = value
            # print(value)
            # print("HERE " + str(self.testVal))
            # print(instance)
            #return value

        slider2 = Slider(
            min = -1500, 
            max = 1500, 
            orientation = 'horizontal',
            value_track = True,
            value_track_color = [1, 0, 0, 1],
            step = 100
            
            )
        label2 = Label()
        popupButton2 = Button(text = "Set Value")
        slider2.bind(value=OnSliderValueChange2)
        box2 = BoxLayout()
        box2.add_widget(slider2)
        box2.add_widget(label2)
        box2.add_widget(popupButton2)
        popup2 = Popup(title = "+ = up, right | - = down, left", content = box2, size_hint = (None, None), size = (400, 100))
        popupButton2.bind(on_press = popup2.dismiss)
        popupButton2.bind(on_press = self.update)


        self.makeDropDown(dropdown, popup, popup2)
        self.makeDropDown(dropdown2, popup, popup2)
        self.makeDropDown(dropdown3, popup, popup2)
        self.makeDropDown(dropdown4, popup, popup2)
        self.makeDropDown(dropdown5, popup, popup2)
        self.makeDropDown(dropdown6, popup, popup2)
        self.makeDropDown(dropdown7, popup, popup2)
        self.makeDropDown(dropdown8, popup, popup2)


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

          

        dropdown.bind(on_select=lambda instance, x: setattr(self.button1, 'text', "Action1: " + x))
        dropdown2.bind(on_select=lambda instance, x: setattr(self.button2, 'text', "Action2: " +x))
        dropdown3.bind(on_select=lambda instance, x: setattr(self.button3, 'text', "Action3: " +x))
        dropdown4.bind(on_select=lambda instance, x: setattr(self.button4, 'text', "Action4: " +x))
        dropdown5.bind(on_select=lambda instance, x: setattr(self.button5, 'text', "Action5: " +x))
        dropdown6.bind(on_select=lambda instance, x: setattr(self.button6, 'text', "Action6: " +x))
        dropdown7.bind(on_select=lambda instance, x: setattr(self.button7, 'text', "Action7: " +x))
        dropdown8.bind(on_select=lambda instance, x: setattr(self.button8, 'text', "Action8: " +x))


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
