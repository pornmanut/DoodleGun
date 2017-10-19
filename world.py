from player import Player
from random import choice
from random import randint
from arcade import color

import platfrom

class Create:
    Edge_x = 20
    Edge_y = 35
    Coin_Y_Offset = 20
    Color_List = [color.REDWOOD,color.FOREST_GREEN,color.FLAX,
                    color.WHITE_SMOKE,color.ALMOND,color.RUBY]
    Move_Speed_List = [1.5,1,0.5,-0.5,-1,-1.5]

    @staticmethod
    def random_spawn(drop_rate):
        random = randint(0,100)
        if(random < drop_rate):
            return True
        return False
    @classmethod
    def random_cloud(cls,width,height,side=''):
        y = randint(height//2+cls.Edge_y,height+height//2-cls.Edge_y)
        scale = choice([0.5,0.6,0.7,0.75,0.8,0.9,1,1.25])
        if(side == 'left'):
            x = -cls.Edge_x
        elif(side == 'right'):
            x = width+cls.Edge_x
        else:
            x = randint(cls.Edge_x,width)
            y = randint(height+height//4+cls.Edge_y,height+height//2+cls.Edge_y)
        return platfrom.Cloud(x,y,scale,side)

    @classmethod
    def generation_cloud(cls,width,height,amount,list_of_cloud):
        for i in range(amount):
            side = choice(['left','right',''])
            list_of_cloud.append(Create.random_cloud(width,height,side))

    @classmethod
    def random_platfrom(cls,x1,y1,x2,y2):
        x = randint(x1+cls.Edge_x,x2-cls.Edge_x)
        y = randint(y1+cls.Edge_y,y2-cls.Edge_y)
        color = choice(cls.Color_List)
        return platfrom.Normal(x,y,color)

    @classmethod
    def random_movable_platfrom(cls,x1,y1,x2,y2):
        x = randint(x1+2*cls.Edge_x,x2-2*cls.Edge_x)
        y = randint(y1+cls.Edge_y,y2-cls.Edge_y)
        color = choice(cls.Color_List)
        move_speed = choice(cls.Move_Speed_List)
        return platfrom.Normal_Moveable(x,y,color,move_speed)

    @classmethod
    def random_coin(cls,x,y,drop_rate,list_of_coin):
        if(cls.random_spawn(drop_rate)):
            list_of_coin.append(platfrom.Coin(x,y+cls.Coin_Y_Offset))

    @staticmethod
    def generation_platfrom(width,height,sector,list_of_platfrom,coin=False,list_of_coin=None,drop_rate=10):
        start = 0
        for i in range(sector):
            list_of_platfrom.append(Create.random_platfrom(0,start,width,start+(2*height)//sector))
            start += (2*height)//sector
            if(coin):
                if(list_of_coin != None):
                    Create.random_coin(list_of_platfrom[i].x,list_of_platfrom[i].y,drop_rate,list_of_coin)


    @classmethod
    def platfrom_system(cls,width,height,sector,amount,list_of_platfrom,coin=False,list_of_coin=None,drop_rate=10):
        start_height = int((2*height)*((sector-amount)/sector))
        for i in range(amount):
            if(cls.random_spawn(drop_rate)):
                list_of_platfrom.append(Create.random_movable_platfrom(0,start_height,width,start_height+(2*height)//sector))
            else:
                list_of_platfrom.append(Create.random_platfrom(0,start_height,width,start_height+(2*height)//sector))
                if(coin):
                    if(list_of_coin != None):
                        Create.random_coin(list_of_platfrom[-1].x,list_of_platfrom[-1].y,drop_rate,list_of_coin)
            start_height += (2*height)//sector

class World:

    SCORE = 0
    SCORE_TEMP = SCORE
    MONEY = 0
    Drop_Rate = 10
    MAX_DROP_RATE = 80
    Drop_Rate_Change = 50

    def __init__(self,width,height):
        #setup
        self.width = width
        self.height = height
        self.sector = ((2*height)//80)-(2*height)//1000
        self.setup()
        self.time = 0
        self.time_status = 0
        self.time_cloud = 0
        self.list_of_platfrom = []
        self.list_of_coin = []
        Create.generation_platfrom(self.width,self.height,self.sector,self.list_of_platfrom,True,self.list_of_coin,World.Drop_Rate)
        self.player = Player(self.list_of_platfrom[0].x,self.list_of_platfrom[0].y+50,self.width,self.height)

        self.list_of_cloud = []
        Create.generation_cloud(self.width,self.height,1,self.list_of_cloud)


    def __repr__(self):
        return '{}x{} sector:{}'.format(self.width,self.height,self.sector)

    @classmethod
    def add_drop_rate(cls):
        if(cls.SCORE > cls.SCORE_TEMP+cls.Drop_Rate_Change and cls.Drop_Rate < cls.MAX_DROP_RATE):
            cls.Drop_Rate += 5
            cls.SCORE_TEMP = cls.SCORE
            return True
        return False


    def setup(self):
        platfrom.Base.Setup(self.width,self.height,self.sector)


    def on_key_press(self,key,modifier):
        self.player.on_key_press(key,modifier)

    def on_key_release(self,key,modifier):
        self.player.on_key_release(key,modifier)

    @classmethod
    def add_score(cls,amount):
        cls.SCORE += amount
    @classmethod
    def add_money(cls,amount):
        cls.MONEY += amount

    def update(self,delta):

        self.time_status += delta
        self.time += delta
        self.time_cloud += delta

        if(len(self.list_of_cloud) < 8 and self.time_cloud > 2):
            Create.generation_cloud(self.width,(3/4)*self.height,1,self.list_of_cloud)
            self.time_cloud = 0

        if(self.list_of_platfrom[0].movement()):
            self.player.movement_w_platfrom()

        for index,cl in enumerate(self.list_of_cloud):
            cl.update()
            if(cl.is_out_of_edge()):
                del self.list_of_cloud[index]

        if(World.add_drop_rate()):
            print("[{:.2f}]----->Change:Drop_Rate {}".format(self.time,World.Drop_Rate))


        if(self.time_status > 3):
            print("Width: {} Height: {} Sector {}".format(self.width,self.height,self.sector))
            print("Platfrom: {} Coin: {}".format(len(self.list_of_platfrom),len(self.list_of_coin)))
            print("Score: {} Money: {}".format(World.SCORE,World.MONEY))
            self.time_status = 0
        self.player.update()

        for index,c in enumerate(self.list_of_coin):
            c.update()
            if(self.player.is_collisions(c,check_y=False)):
                print("[{:.2f}]----->Got: Coin {}".format(self.time,self.list_of_coin[index]))

                World.add_money(c.coin)
                World.add_score(c.coin)

                print("[{:.2f}]----->Money +{}".format(self.time,c.coin))
                print("[{:.2f}]----->Score +{}".format(self.time,c.coin))

                del self.list_of_coin[index]
            elif(c.is_out_of_edge()):

                print("[{:.2f}]----->Remove: Coin {}".format(self.time,self.list_of_coin[index]))

                del self.list_of_coin[index]

        for index,pf in enumerate(self.list_of_platfrom):
            pf.update(delta)
            if(pf.is_out_of_edge()):

                print("[{:.2f}]----->Remove: Platfrom {}".format(self.time,self.list_of_platfrom[index]))

                del self.list_of_platfrom[index]

            if(self.player.is_collisions(pf)):
                self.player.jump()

                print("[{:.2f}]----->Player Jump at {}".format(self.time,pf))

                if(index > 1):

                    print("[{:.2f}]----->Score +{}".format(self.time,index))

                    for cl in self.list_of_cloud:
                        cl.set_movement(index-1)
                    for pf in self.list_of_platfrom:
                        pf.set_movement(index-1)
                    for c in self.list_of_coin:
                        c.set_movement(index-1)

                    Create.platfrom_system(self.width,self.height,self.sector,index-1,self.list_of_platfrom,True,self.list_of_coin,World.Drop_Rate)
                    World.add_score(index)
