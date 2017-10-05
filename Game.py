import arcade
import player
import world

#Window setting
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.AZURE
WINDOWS_TITLE = 'Game.py'


class Window(arcade.Window):

    def __init__(self,width,height):
        super().__init__(width,height,WINDOWS_TITLE)



    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(BACKGROUND_COLOR)



def main():
    game = Window(SCREEN_WIDTH,SCREEN_HEIGHT)
    #run
    arcade.run()

if __name__ == '__main__':
    main()
    #def update(self,delta):
