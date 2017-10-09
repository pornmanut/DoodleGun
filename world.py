from player import Player
from random import randint

import platfrom


class Control:
    def remove_first(i_list,amount):
        for i in range(amount):
            del i_list[0]
        return i_list



class Create:
    Edge = 10
    @classmethod
    def random_platfrom(cls,x1,y1,x2,y2):
        x = randint(x1+cls.Edge,x2-cls.Edge)
        y = randint(y1+cls.Edge,y2-cls.Edge)
        return platfrom.Normal(x,y)
    @staticmethod
    def sector_platfrom(width,height,sector,list_of_platfrom):
        height *= 2
        start = 0
        for i in range(sector):
            list_of_platfrom.append(Create.random_platfrom(0,start,width,start+height//sector))
            start += height//sector
        return list_of_platfrom
    @staticmethod
    def add_platfrom(width,height,sector,amount,list_of_platfrom):
        height *= 2
        start_height = int(height*((sector-amount)/sector))
        for i in range(amount):
            list_of_platfrom.append(Create.random_platfrom(0,start_height,width,start_height+height//sector))
            start_height += height//sector
        return list_of_platfrom


class World:
    SCORE = 0
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.sector = 18
        self.list_of_platfrom = []
        self.list_of_platfrom = Create.sector_platfrom(self.width,self.height,self.sector,self.list_of_platfrom)
        self.player = Player(self.list_of_platfrom[0].x,self.list_of_platfrom[0].y+50
                                ,self.width,self.height)
        self.list_update = False
        self.list_update_move = 0
        #print(self.list_of_platfrom)

    def on_key_press(self,key,modifier):
        self.player.on_key_press(key,modifier)

    def on_key_release(self,key,modifier):
        self.player.on_key_release(key,modifier)

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
        create = False
        #print(self.player)
        self.player.update(delta)
        for index,item in enumerate(self.list_of_platfrom):

            item.update(delta)

            if(self.is_player_collisions(self.player,item)):

                print('index: {}'.format(index))
                self.player.jump()
                self.player.delta_y -= 3*index

                if(index != 0):
                    self.player.move = index
                    World.SCORE += index
                    for pf in self.list_of_platfrom:
                        pf.move = index

                    Control.remove_first(self.list_of_platfrom,index)

                    self.list_update_move = index
                    self.list_update = True

                    self.list_of_platfrom = Create.add_platfrom(self.width,self.height,self.sector,index,self.list_of_platfrom)

                    #self.player.y = self.list_of_platfrom[0].y+self.list_of_platfrom[0].height+self.player.size-(index*self.height//9)
