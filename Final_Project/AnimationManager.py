from turtle import update
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from kivy.clock import Clock


# KV = '''
# Image:
#     source: 'face1.png'
# Window:


# '''

class AnimationManager(Image):
    #anim = Animation()
    image1 = Image(source='face1.png')
    def __init__(self):
        print("Initialized: AnimationManager")
        
        
    def NoAnimation(self):
        return self.image1
        print("Animation: none")

    def Talking(self):
        print("Animation: talking")
        #anim = Animation(pos =(0, 0), t='out_bounce')
        #anim += Animation(pos =(0, 330), t='out_bounce')

    def Moving(self):

        print("Animation: moving")

    def Hurt(self):
        print("Animation: hurt")

    def Attack(self):
        print("Animation: attack")

    def FoundKey(self):
        print("Animation: found key")

    def Healed(self):
        print("Animetion: healed")

    def Victory(self):
        print("Animation: victory")

class WindowApp(App):

    def build(self):
        
        Window.size = (800, 480)
        self.image1 = Image(source='face1.png')
        
        return self.image1



class Talking(App):

    def animate(self, something):
        ani = Animation()
        ani.start(self.image1)
        ani.on_complete(self.stop())

    def build(self):
        Window.size = (800, 480)
        self.image1 = Image(source='talk.zip', anim_delay=1/5, anim_loop = 10)
        Clock.schedule_interval(self.animate,5)
        return self.image1

class TakeDamage(App):

    def animate(self, something):
        ani = Animation()
        ani.start(self.image1)
        ani.on_complete(self.stop())
        


    def build(self):
        Window.size = (800, 480)
        
        self.image1 = Image(source='damage.zip', anim_delay=1/2, anim_loop = 1)
        Clock.schedule_interval(self.animate,2)

        return self.image1

        
  



