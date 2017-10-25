import arcade
import draw
from world import World

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = arcade.color.AZURE
WINDOWS_TITLE = 'Game.py'
EDGE_WIDTH = SCREEN_WIDTH//10
EDGE_HEIGHT = SCREEN_HEIGHT//20
UPDATE_BACKGROUND_SCORE = 50

class Window(arcade.Window):

    def __init__(self,width,height):
        super().__init__(width,height,WINDOWS_TITLE)

        self.world = World(width,height)
        self.setup()


    def setup(self):
        self.background = BACKGROUND_COLOR
        arcade.set_background_color(self.background)
        self.background_change_time = 0
        self.score_to_change_background = 0
        self.is_background_change = False

    def draw_score(self):
        text = arcade.create_text('Score:{}'.format(self.world.SCORE),color=arcade.color.WHITE,
                                    font_size=14,anchor_x='center',align='center')
        text_offset = arcade.create_text('Score:{}'.format(self.world.SCORE),color=arcade.color.BLACK,
                                    font_size=14,anchor_x='center',align='center')

        arcade.render_text(text_offset,EDGE_WIDTH+2,SCREEN_HEIGHT-EDGE_HEIGHT-2)
        arcade.render_text(text,EDGE_WIDTH,SCREEN_HEIGHT-EDGE_HEIGHT)


    def draw_time(self):
        text = arcade.create_text('Time:{:.1f}'.format(self.world.time),color=arcade.color.WHITE,
                                    font_size=14,anchor_x='center',align='center')
        text_offset = arcade.create_text('Time:{:.1f}'.format(self.world.time),color=arcade.color.BLACK,
                                    font_size=14,anchor_x='center',align='center')
        arcade.render_text(text_offset,SCREEN_WIDTH-EDGE_WIDTH+2,SCREEN_HEIGHT-EDGE_HEIGHT-2)
        arcade.render_text(text,SCREEN_WIDTH-EDGE_WIDTH,SCREEN_HEIGHT-EDGE_HEIGHT)
    def on_draw(self):
        arcade.start_render()

        if(self.is_background_change):
            arcade.set_background_color(self.background)

        self.draw_score()
        self.draw_time()

        self.draw_platfrom()
        self.draw_coin()
        self.draw_cloud()
        self.draw_player()

        if(self.world.pause):
            self.draw_lose_window()
        #see platfrom 3

    def draw_cloud(self):
        for cl in self.world.list_of_cloud:
            draw.Draw_Cloud(cl).draw()

    def draw_player(self):
        draw.Draw_Player(self.world.player).draw()

    def draw_coin(self):
        for c in self.world.list_of_coin:
            draw.Draw_Circle(c).draw()

    def draw_platfrom(self):
        for pf in self.world.list_of_platfrom:
            draw.Draw_Rectangle(pf).draw()

    def draw_lose_window(self):
        draw.Blackground_Title(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,300,250,'Hello',score=self.world.SCORE).draw()

    def on_key_press(self,key,modifier):
        self.world.on_key_press(key,modifier)

    def on_key_release(self,key,modifier):
        self.world.on_key_release(key,modifier)

    def update_background(self):

        if(self.world.restart == True):
            self.setup()

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
