from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.image import Image


# KV = '''
# Image:
#     source: 'face1.png'
# Window:


# '''

class AnimationManager:
    #anim = Animation()
    
    def __init__(self):
        print("Initialized: AnimationManager")
        self.Window = Image(source='face1.png')
        Window.size = (800, 480)
        
    def NoAnimation(self):
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
