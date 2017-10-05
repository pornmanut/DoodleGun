import arcade
import draw
from world import World

#Window setting
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000
BACKGROUND_COLOR = arcade.color.AZURE
WINDOWS_TITLE = 'Game.py'


class Window(arcade.Window):

    def __init__(self,width,height):
        super().__init__(width,height,WINDOWS_TITLE)
        arcade.set_background_color(BACKGROUND_COLOR)
        self.world = World(width,height)
        self.player_sprite = draw.Draw_Circle(self.world.player)


    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()


    def update(self,delta):
        self.world.update(delta)



def main():
    game = Window(SCREEN_WIDTH,SCREEN_HEIGHT)
    #run
    arcade.run()

if __name__ == '__main__':
    main()
    #def update(self,delta):
