from arcade import color

MOVEMENT_SPEED = 5
CIRCLE_RADIUS = 20
CIRCLE_COLOR = color.ALICE_BLUE
GRAVITY = 0.3

class Player:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = CIRCLE_RADIUS
        self.color = CIRCLE_COLOR
    def update(self,delta):
        self.x += MOVEMENT_SPEED
