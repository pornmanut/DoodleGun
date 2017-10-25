from arcade import color
from random import randint
from random import choice

COLOR = color.WHITE_SMOKE
WIDTH = 96
HEIGHT = 6
EDGE = 50

class Base:

    #seting with setup
    Screen_Height = 0
    Screen_Width = 0
    Sector = 1
    Sector_Width = 0
    MOVE_SPEED = 8

    @classmethod
    def Setup(cls,screen_width,screen_height,sector):
        cls.Screen_Width = screen_width
        cls.Screen_Height = screen_height
        cls.Sector = sector
        cls.Sector_Width = 2*screen_height//sector

    def __init__(self,x,y,width=None,height=None):

        self.x = x
        self.y = y
        #width,height of platfrom
        self.width = width
        self.height = height
        self.color = COLOR
        self.angle = 0
        #when move how y is decresed
        self.move = 0
        self.move_target = 0
    def __repr__(self):
        #Base(x,y)
        return 'Base({:.2f},{:.2f})'.format(self.x,self.y)

    def set_movement(self,move):
        self.move = move
        self.move_target = move*Base.Sector_Width

    def movement(self):
        if(self.move > 0):
            if(self.move_target-Base.MOVE_SPEED >= 0):
                self.y -= Base.MOVE_SPEED
                self.move_target -= Base.MOVE_SPEED
                return True
            else:
                self.y -= self.move_target
                self.move_target = 0
                self.move = 0
                return False
        return False

    def is_out_of_edge(self):
        if(self.y < 0):
            return True
        return False

    def update(self):
        #Trigger from world
        self.movement()


class Normal(Base):
    def __init__(self,x,y,color):
        super().__init__(x,y,WIDTH,HEIGHT)
        self.color = color
    def __repr__(self):
        return 'Normal({:.2f},{:.2f}) RGB: {}'.format(self.x,self.y,self.color)

    def update(self,delta):
        super().update()

class Normal_Moveable(Normal):

    def __init__(self,x,y,color,move_speed):
        super().__init__(x,y,color)
        self.move_speed = move_speed
        self.time = 0
        self.time_change = 1

    def __repr__(self):
        return 'Moving({:.2f},{:.2f}) RGB:{} Speed: {}'.format(self.x,self.y,
                self.color,self.move_speed)

    def sign_move(self):
        if(self.time > self.time_change):
            self.move_speed *= -1
            self.time = 0
        self.x += self.move_speed

    def update(self,delta):
        super().update(delta)
        self.time += delta
        self.sign_move()


class Coin(Base):
    def __init__(self,x,y,size=8,coin=5):
        self.size = size
        self.coin = coin
        super().__init__(x,y)
        self.width = 4*self.size
        self.height = 4*self.size
        self.color = color.WHEAT

    def __repr__(self):
        return 'Coin({:.2f},{:.2f})'.format(self.x,self.y)

    def update(self):
        super().update()

class Cloud(Base):
    def __init__(self,x,y,scale,side='right'):
        super().__init__(x,y)
        self.scale = scale
        self.size = 8*self.scale
        self.color = (255,255,255)
        self.random_x1 = self.x-self.size-randint(int(5*self.scale),int(15*self.scale))
        self.random_x2 = self.x+self.size+randint(int(5*self.scale),int(15*self.scale))
        self.side = side

        if(self.side == 'left'):
            self.random_move = choice([0.25,0.5,1,1.5,2])
        elif(self.side == 'right'):
            self.random_move = -choice([0.25,0.5,1,1.5,2])
        else:
            self.random_move = 0
    def __repr__(self):
        return 'Cloud({:.2f},{:.2f})'.format(self.x,self.y)

    def movement(self):
        self.x += self.random_move
        self.random_x1 += self.random_move
        self.random_x2 += self.random_move
        super().movement()

    def is_out_of_edge(self):
        if(self.side == 'left' and self.x > Base.Screen_Width+3*self.size) or (self.side == 'right' and self.x < -3*self.size) or (self.y < 0):
            return True
        return False

    def update(self):
        super().update()
