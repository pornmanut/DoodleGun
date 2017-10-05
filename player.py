from arcade import color

MOVEMENT_SPEED = 5
CIRCLE_RADIUS = 20
CIRCLE_COLOR = color.ALICE_BLUE
JUMP_SPEED = 10
GRAVITY = 0.1

class Player:

    def __init__(self,x,y,screen_width,screen_height):
        self.x = x
        self.y = y
        self.delta_x = MOVEMENT_SPEED
        self.delta_y = 0
        self.size = CIRCLE_RADIUS
        self.color = CIRCLE_COLOR
        self.screen_width = screen_width
        self.screen_height = screen_height
    def update(self,delta):

        self.delta_y += -GRAVITY

        self.x += self.delta_x
        self.y += self.delta_y

        if(self.x < self.size/2):
            self.x = self.screen_width-self.size/2
        elif(self.x > self.screen_width-self.size/2):
            self.x = self.size/2

        if(self.y < 0 and self.delta_y < 0):
            self.y = self.screen_height
