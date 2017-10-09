from player import Player
from random import randint

import platfrom

class Create:
    Edge = 10
    @classmethod
    def random_platfrom(cls,x1,y1,x2,y2):
        x = randint(x1+cls.Edge,x2-cls.Edge)
        y = randint(y1+cls.Edge,y2-cls.Edge)
        return platfrom.Normal(x,y)

    @staticmethod
    def generation_platfrom(width,height,sector,list_of_platfrom):
        start = 0
        for i in range(sector):
            list_of_platfrom.append(Create.random_platfrom(0,start,width,start+(2*height)//sector))
            start += (2*height)//sector

    @staticmethod
    def platfrom_system(width,height,sector,amount,list_of_platfrom):
        start_height = int((2*height)*((sector-amount)/sector))
        for i in range(amount):
            del list_of_platfrom[0]
            list_of_platfrom.append(Create.random_platfrom(0,start_height,width,start_height+(2*height)//sector))
            start_height += (2*height)//sector


class World:
    SCORE = 0
    def __init__(self,width,height):
        #setup
        self.width = width
        self.height = height
        self.sector = ((2*height)//80)-(2*height)//1000
        self.setup()

        self.list_of_platfrom = []
        Create.generation_platfrom(self.width,self.height,self.sector,self.list_of_platfrom)

        self.player = Player(self.list_of_platfrom[0].x,self.list_of_platfrom[0].y+50,self.width,self.height)


    def __repr__(self):
        return '{}x{} sector:{}'.format(self.width,self.height,self.sector)

    def setup(self):
        platfrom.Base.Setup(self.width,self.height,self.sector)


    def on_key_press(self,key,modifier):
        self.player.on_key_press(key,modifier)

    def on_key_release(self,key,modifier):
        self.player.on_key_release(key,modifier)

    def update(self,delta):

        self.player.update()
        for index,pf in enumerate(self.list_of_platfrom):
            pf.update()
            if(self.player.is_collisions(pf)):
                self.player.jump(index)
                if(index != 0):
                    for pf in self.list_of_platfrom:
                        pf.move = index

                    Create.platfrom_system(self.width,self.height,self.sector,index,self.list_of_platfrom)
                    World.SCORE += index
