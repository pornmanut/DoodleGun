import arcade
from arcade import color
import draw
COLOR = color.AERO_BLUE
WIDTH = 100
HEIGHT = 10
SCREEN_HEIGHT = 1000
class Base:

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = COLOR
        self.angle = 0

        self.isMove = False
        self.move = 1
    def __repr__(self):
        return '[{},{}]'.format(self.x,self.y)

    def update(self,delta):
        if(self.isMove):
            self.y -= self.move*SCREEN_HEIGHT//9
            self.isMove = False
            self.move = 1

class Normal(Base):
    def __init__(self,x,y):
        super().__init__(x,y,WIDTH,HEIGHT)
