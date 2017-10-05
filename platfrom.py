from arcade import color


COLOR = color.AERO_BLUE
WIDTH = 100
HEIGHT = 10

class Base:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = COLOR
        self.angle = 0

        self.isMoving = False
        self.moving = 0
    def out_of_edge(self):
        if(self.y < y+self.height//2):
            return True
        return False
    def update(self,delta):
        if(self.isMoving):
            self.y += self.moving
            self.moving = 0
            self.isMoving = False


class Normal(Base):
    def __init__(self,x,y):
        super().__init__(x,y,WIDTH,HEIGHT)
