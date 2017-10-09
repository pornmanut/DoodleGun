import arcade
import draw
from world import World

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = arcade.color.AZURE
WINDOWS_TITLE = 'Game.py'
EDGE_WIDTH = SCREEN_WIDTH//20
EDGE_HEIGHT = SCREEN_HEIGHT//20

class Window(arcade.Window):

    def __init__(self,width,height):
        super().__init__(width,height,WINDOWS_TITLE)
        arcade.set_background_color(BACKGROUND_COLOR)

        self.world = World(width,height)
        self.player_sprite = draw.Draw_Circle(self.world.player)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('SCORE:{}'.format(World.SCORE),EDGE_WIDTH,EDGE_HEIGHT,arcade.color.WHITE,12)

        self.player_sprite.draw()
        for pf in self.world.list_of_platfrom:
            draw.Draw_Rectangle(pf).draw()


    def on_key_press(self,key,modifier):
        self.world.on_key_press(key,modifier)

    def on_key_release(self,key,modifier):
        self.world.on_key_release(key,modifier)

    def update(self,delta):
        self.world.update(delta)


def main():
    game = Window(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()
