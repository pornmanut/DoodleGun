from arcade import color
import arcade.key

MOVEMENT_SPEED = 4.5
CIRCLE_RADIUS = 20
CIRCLE_COLOR = color.ALICE_BLUE
JUMP_SPEED = 12
GRAVITY = 0.3
FICTION = 0.05

class Player:

    def __init__(self,x,y,screen_width,screen_height):
        self.x = x
        self.y = y
        self.delta_x = 0
        self.delta_y = 0
        self.size = CIRCLE_RADIUS
        self.color = CIRCLE_COLOR
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.jump_speed = JUMP_SPEED
    def out_of_edge(self):
        if(self.x < self.size/2):
            self.x = self.screen_width-self.size/2
        elif(self.x > self.screen_width-self.size/2):
            self.x = self.size/2

    def on_key_press(self,key,modifier):
        if(key == arcade.key.LEFT):
            self.delta_x = -MOVEMENT_SPEED
        elif(key == arcade.key.RIGHT):
            self.delta_x = MOVEMENT_SPEED

    def fiction(self):
        if(self.delta_x > FICTION):
            self.delta_x -= FICTION
        elif(self.delta_x < -FICTION):
            self.delta_x += FICTION
        else:
            self.delta_x = 0

    def jump(self):
        self.delta_y = JUMP_SPEED

    def update(self,delta):

        self.delta_y += -GRAVITY

        self.x += self.delta_x
        self.y += self.delta_y

        self.out_of_edge()
        self.fiction()
        if(self.y < 0 and self.delta_y < 0):
            self.jump()
