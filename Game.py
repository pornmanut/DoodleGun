import arcade
import draw
from world import World

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = arcade.color.AZURE
WINDOWS_TITLE = 'Game.py'
EDGE_WIDTH = SCREEN_WIDTH//20
EDGE_HEIGHT = SCREEN_HEIGHT//20
UPDATE_BACKGROUND_SCORE = 50

class Window(arcade.Window):

    def __init__(self,width,height):
        super().__init__(width,height,WINDOWS_TITLE)
        self.background = BACKGROUND_COLOR
        arcade.set_background_color(self.background)

        self.background_change_time = 0
        self.score_to_change_background = 0
        self.is_background_change = False
        self.world = World(width,height)
        self.player_sprite = draw.Draw_Circle(self.world.player)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(self.background)
        arcade.draw_text('Score:{}'.format(self.world.SCORE),EDGE_WIDTH,EDGE_HEIGHT,arcade.color.WHITE,12)
        arcade.draw_text('Money:{}'.format(self.world.MONEY),EDGE_WIDTH,EDGE_HEIGHT*2,arcade.color.WHITE,12)
        arcade.draw_text('Time:{:.0f}'.format(self.world.time),EDGE_WIDTH,EDGE_HEIGHT*3,arcade.color.WHITE,12)

        #see platfrom 3
        for pf in self.world.list_of_platfrom:
            draw.Draw_Rectangle(pf).draw()
        #see coin 2
        for c in self.world.list_of_coin:
            draw.Draw_Circle(c).draw()
        #see player 1
        self.player_sprite.draw()


    def on_key_press(self,key,modifier):
        self.world.on_key_press(key,modifier)

    def on_key_release(self,key,modifier):
        self.world.on_key_release(key,modifier)

    def update_background(self):

        if(self.world.SCORE > UPDATE_BACKGROUND_SCORE+self.score_to_change_background):
            self.is_background_change = True
            self.score_to_change_background = self.world.SCORE

            print("[{:.2f}]----->Blackground Change".format(self.world.time))

        if(self.background_change_time < 20 and self.is_background_change):
            self.background = draw.Background.get_darkness_to_background(self.background)
            self.background_change_time += 1
        else:
            self.is_background_change = False
            self.background_change_time = 0



    def update(self,delta):
        self.update_background()
        self.world.update(delta)





def main():
    game = Window(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()
