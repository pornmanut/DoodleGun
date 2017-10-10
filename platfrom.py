from arcade import color


COLOR = color.WHITE_SMOKE
MOVE_SPEED = 5
WIDTH = 80
HEIGHT = 6


class Base:

    #seting with setup
    Screen_Height = 0
    Screen_Width = 0
    Sector = 1

    @classmethod
    def Setup(cls,screen_width,screen_height,Sector):
        cls.Screen_Width = screen_width
        cls.Screen_Height = screen_height
        cls.Sector = Sector

    def __init__(self,x,y,width,height):

        self.x = x
        self.y = y
        #width,height of platfrom
        self.width = width
        self.height = height
        self.color = COLOR
        self.angle = 0
        #player pass how many platfrom
        self.move = 0
        #when move how y is decresed
        self.move_target = 0
        #move with speed
        self.move_speed = MOVE_SPEED
        #tempolary move
        self.move_temp = self.move

    def __repr__(self):
        #Base(x,y)
        return 'Base({:.2f},{:.2f})'.format(self.x,self.y)



    def set_target(self):
        if(self.move > 0):
            self.move_target = self.move*((2*Base.Screen_Height)//Base.Sector)
            self.move_temp = self.move
            self.move = 0

    def movement(self):
        if(self.move_temp > 0):
            if(self.move_target-self.move_temp*self.move_speed >= 0):
                #- move speed
                self.y -= self.move_temp*self.move_speed
                # remain move_target and continum
                self.move_target -= self.move_temp*self.move_speed
            elif(self.move_target-self.move_temp*self.move_speed < 0):
                #- move target remain
                self.y -= self.move_target
                # set move to zero no more move
                self.move_temp = 0
            else:
                #set nove_target to zero no more move
                self.move_temp = 0


    def update(self):
        #Trigger from world
        self.set_target()
        self.movement()


class Normal(Base):
    def __init__(self,x,y):
        super().__init__(x,y,WIDTH,HEIGHT)

    def __repr__(self):
        return 'Normal({:.2f},{:.2f})'.format(self.x,self.y)
