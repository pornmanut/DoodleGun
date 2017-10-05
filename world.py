from player import Player
from random import randint
import platfrom

class Create:
    @staticmethod
    def create_random_platfrom(x1,y1,x2,y2,amount):
        product = []
        for index in range(amount):
            x = randint(x1,x2)
            y = randint(y1,y2)
            product.append(platfrom.Normal(x,y))
        return product

class World:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.player = Player(100,100,self.width,self.height)

        self.list_of_platfrom = []
        self.list_of_platfrom = Create.create_random_platfrom(0,0,width,height,10)

    def on_key_press(self,key,modifier):
        self.player.on_key_press(key,modifier)

    def is_player_collisions(self,player,other):
        if(player.delta_y <0 and
            player.y-player.size <= other.y+other.height and
            player.y-player.size >= other.y-other.height and
            player.x-player.size <= other.x+other.width//2 and
            player.x+player.size >= other.x-other.width//2):
            return True
        else:
            return False

    def update(self,delta):

        self.player.update(delta)
        for item in self.list_of_platfrom:
            if(self.is_player_collisions(self.player,item)):
                self.player.jump()
