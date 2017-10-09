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
        #position x,y
        self.x = x
        self.y = y
        #detal x,y
        self.delta_x = 0
        self.delta_y = 0
        #size of circle
        self.size = CIRCLE_RADIUS
        #color of player
        self.color = CIRCLE_COLOR
        #screen width,height
        self.screen_width = screen_width
        self.screen_height = screen_height
        #jump
        self.jump_speed = JUMP_SPEED
        #is preseed key right or ledt
        self.isKeyRight = False
        self.isKeyLeft = False

    def __repr__(self):
        #show [x,y]->[delta_x,delta_y]
        return "[{:.2f},{:.2f}]->[{:.2f},{:.2f}]".format(self.x,self.y,self.delta_x,self.delta_y)

    def out_of_edge(self):
        #x
        if(self.x < self.size//2):
            self.x = self.screen_width-self.size//2
        elif(self.x > self.screen_width-self.size//2):
            self.x = self.size//2

        #y
        # if(self.y < 0 and self.delta_y < 0):
        #     self.jump()

    def on_key_press(self,key,modifier):
        if(key == arcade.key.LEFT):
            self.isKeyLeft = True
        elif(key == arcade.key.RIGHT):
            self.isKeyRight = True

    def on_key_release(self,key,modifier):
        if(key == arcade.key.LEFT and self.isKeyLeft):
            self.isKeyLeft = False
        elif(key == arcade.key.RIGHT and self.isKeyRight):
            self.isKeyRight = False


    def movement(self):
        if(self.isKeyLeft):
            self.delta_x = -MOVEMENT_SPEED
        elif(self.isKeyRight):
            self.delta_x = MOVEMENT_SPEED
        else:
            self.fiction()

    def fiction(self):
        if(not(self.isKeyLeft and self.isKeyRight)):
            if(self.delta_x > FICTION):
                self.delta_x -= FICTION
            elif(self.delta_x < -FICTION):
                self.delta_x += FICTION
            else:
                self.delta_x = 0


    def jump(self):
        self.delta_y = JUMP_SPEED

    def gravity(self):
        self.delta_y += -GRAVITY

    def update(self,delta):

        self.gravity()
        self.movement()
        self.fiction()
        #change xand y per update
        self.x += self.delta_x
        self.y += self.delta_y

        self.out_of_edge()
