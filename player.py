from arcade import color
import arcade.key

MOVEMENT_SPEED = 6
CIRCLE_RADIUS = 12
CIRCLE_COLOR = color.WHEAT
COLOR = (134,1,17,200)
JUMP_SPEED = 8

GRAVITY = 0.3
FICTION = 0.3

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
        self.color_2 = COLOR
        #screen width,height
        self.screen_width = screen_width
        self.screen_height = screen_height
        #jump
        self.jump_speed = JUMP_SPEED
        self.mutiply_speed = 1/2
        #is preseed key right or ledt
        self.isKeyRight = False
        self.isKeyLeft = False

    def __repr__(self):
        #show [x,y]->[delta_x,delta_y]
        return "[{:.2f},{:.2f}]->[{:.2f},{:.2f}]".format(self.x,self.y,self.delta_x,self.delta_y)

    def is_collisions(self,other,check_y=True):
        if(check_y and self.delta_y > 0):
            return False
        if( self.y-self.size <= other.y+other.height//2+self.size//2 and
            self.y-self.size >= other.y-other.height//2-self.size//2 and
            self.x-self.size <= other.x+other.width//2 and
            self.x+self.size >= other.x-other.width//2   ):
            return True
        else:
            return False

    def out_of_edge(self):
        #x
        if(self.x < self.size//2):
            self.x = self.screen_width-self.size//2
        elif(self.x > self.screen_width-self.size//2):
            self.x = self.size//2

        if(self.y < -self.size and self.delta_y < 0):
            return True
        return False

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

    def movement_w_platfrom(self):
            self.y += -8

    def jump(self,amount=0):
        mutiply = 1
        if(amount > 0):
            mutiply *= self.mutiply_speed

        self.delta_y = JUMP_SPEED*mutiply

    def gravity(self):
        self.delta_y += -GRAVITY

    def update(self):

        self.gravity()
        self.movement()
        self.fiction()
        #change xand y per update
        self.x += self.delta_x
        self.y += self.delta_y

        self.out_of_edge()
