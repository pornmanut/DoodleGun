import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Window(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)
        arcade.set_background_color(arcade.color.RICH_BRILLIANT_LAVENDER)

    def on_key_press(self,key,key_modifiers):

    def update(self,delta):


    def on_draw(self):
        arcade.start_render()

def main():
    window = Window(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
    print("HELLO")
