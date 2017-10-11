from arcade import color


COLOR = color.WHITE_SMOKE
WIDTH = 80
HEIGHT = 6


class Base:

    #seting with setup
    Screen_Height = 0
    Screen_Width = 0
    Sector = 1
    Sector_Width = 0
    MOVE_SPEED = 7

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
            else:
                self.y -= self.move_target
                self.move_target = 0
                self.move = 0

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
