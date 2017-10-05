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
        self.list_of_all_sprite = []
        for item in self.world.list_of_platfrom:
            self.list_of_all_sprite.append(draw.Draw_Rectangle(item))

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        for item in self.list_of_all_sprite:
            item.draw()


    def on_key_press(self,key,modifier):
        self.world.on_key_press(key,modifier)

    def update(self,delta):
        self.world.update(delta)



def main():
    game = Window(SCREEN_WIDTH,SCREEN_HEIGHT)
    #run
    arcade.run()

if __name__ == '__main__':
    main()
    #def update(self,delta):
