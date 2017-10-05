from player import Player

class World:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.player = Player(100,100)

    def update(self,delta):
        self.player.update(delta)
