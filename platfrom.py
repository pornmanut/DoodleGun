import arcade
from arcade import color
import draw

COLOR = color.AERO_BLUE
MOVE_SPEED = 10

SCREEN_HEIGHT = 1000
SECTOR = 18

class Base:

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = COLOR
        self.angle = 0
        self.move = 0
        self.move_target = 0
        self.move_speed = 10
        self.move_temp = self.move
    def __repr__(self):
        return '[{},{}]'.format(self.x,self.y)

    def movement(self):

        if(self.move > 0):
            self.move_target = self.move*((2*SCREEN_HEIGHT)//SECTOR)
            self.move_temp = self.move
            self.move = 0

        if(self.move_target-self.move_temp*self.move_speed >= 0):
            self.y -= self.move_temp*self.move_speed
            self.move_target -= self.move_temp*self.move_speed
        elif(self.move_target-self.move_temp*self.move_speed < 0):
            self.y -= self.move_target
            self.move_target = 0
        else:
            self.move_target = 0


    def update(self,delta):
        self.movement()


class Normal(Base):
    def __init__(self,x,y):
        super().__init__(x,y,100,10)
