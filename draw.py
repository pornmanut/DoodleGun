import arcade

class Background:
    @staticmethod
    def get_darkness_to_background(color):
        new_color = ()
        for c in color:
            c -= 1
            new_color += (c,)
        return new_color

class Draw_Cloud:
    def __init__(self,model):
        self.model = model

    def draw(self):
        arcade.draw_circle_filled(self.model.x,self.model.y,2*self.model.size,self.model.color)
        arcade.draw_circle_filled(self.model.random_x1,self.model.y-self.model.size,self.model.size,self.model.color)
        arcade.draw_circle_filled(self.model.random_x2,self.model.y-self.model.size,self.model.size,self.model.color)
        arcade.draw_lrtb_rectangle_filled(self.model.random_x1,self.model.random_x2,self.model.y,self.model.y-2*self.model.size,self.model.color)


class Draw_Circle:
    def __init__(self,model):
        self.model = model

    def __repr__(self):
        return 'Circle({:.2f},{:.2f})'.format(self.x,self.y)

    def draw(self):
        arcade.draw_circle_filled(self.model.x,self.model.y,
                                    self.model.size,self.model.color)

class Draw_Player(Draw_Circle):
    def __init__(self,model):
        super().__init__(model)

    def __repr__(self):
        return 'Player({:.2f},{:.2f})'.format(self.x,self.y)

    def draw(self):
        super().draw()
        # arcade.draw_lrtb_rectangle_filled(self.model.x-self.model.size,
        #                                 self.model.x+self.model.size,self.model.y,
        #                                 self.model.y-self.model.size,self.model.color_2)

class Draw_Rectangle:
    def __init__(self,model):
        self.model = model

    def __repr__(self):
        return 'Rectangle({:.2f},{:.2f})'.format(self.x,self.y)

    def draw(self):
        arcade.draw_rectangle_filled(self.model.x,self.model.y,
                                        self.model.width-10,self.model.height,
                                        self.model.color,self.model.angle)
        arcade.draw_arc_filled(self.model.x-self.model.width//2+8,self.model.y
                                ,self.model.width//10,self.model.height//2
                                ,self.model.color,90,270)
        arcade.draw_arc_filled(self.model.x+self.model.width//2-8,self.model.y
                                ,self.model.width//10,self.model.height//2
                                ,self.model.color,-90,90)

class Blackground_Title:
    Filled_Color = (255,255,255,220)
    Outline_Color = (0,0,0,220)
    @classmethod
    def __init__(self,x,y,width,height,titlename='title',time=None,score=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.titlename = titlename

        if(time == None):
            self.time = 0
        else:
            self.time = time

        if(score == None):
            self.score = 0
        else:
            self.score = score
        self.text_title = arcade.create_text("Game Over",Blackground_Title.Outline_Color,20,align="center",anchor_x="center")
        self.text_score = arcade.create_text("{}".format(self.score),Blackground_Title.Outline_Color,40,align="center",anchor_x="center")
        self.text_title2 = arcade.create_text("Press space bar to restart...",Blackground_Title.Outline_Color,14,align="center",anchor_x="center")
    def __repr__(self):
        return 'Title {}'

    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.width,self.height,Blackground_Title.Filled_Color)
        arcade.draw_rectangle_outline(self.x,self.y,self.width,self.height,Blackground_Title.Outline_Color)
        arcade.draw_line
        arcade.render_text(self.text_title,self.x,self.y)
        arcade.render_text(self.text_title2,self.x,self.y-80)
        arcade.render_text(self.text_score,self.x,self.y+50)
