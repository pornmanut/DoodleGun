import arcade


#Window setting
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.AZURE



class Window:

    def __init__(self,width,height):

        self.width = width
        self.height = height
        self.title = "game"
        super().__init__(self.width,self.height,self.title)


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
