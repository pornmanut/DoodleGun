import arcade

class Background:
    @staticmethod
    def get_darkness_to_background(color):
        new_color = ()
        for c in color:
            c -= 1
            new_color += (c,)
        return new_color



class Draw_Circle:
    def __init__(self,model):
        self.model = model

    def __repr__(self):
        return 'Circle({:.2f},{:.2f})'.format(self.x,self.y)

    def draw(self):
        arcade.draw_circle_filled(self.model.x,self.model.y,
                                    self.model.size,self.model.color)
class Draw_Rectangle:
    def __init__(self,model):
        self.model = model

    def __repr__(self):
        return 'Rectangle({:.2f},{:.2f})'.format(self.x,self.y)

    def draw(self):
        arcade.draw_rectangle_filled(self.model.x,self.model.y,
                                        self.model.width-10,self.model.height,
                                        self.model.color,self.model.angle)
        arcade.draw_arc_filled(self.model.x-self.model.width//2+10,self.model.y
                                ,self.model.width//10,self.model.height//2
                                ,self.model.color,90,270)
        arcade.draw_arc_filled(self.model.x+self.model.width//2-10,self.model.y
                                ,self.model.width//10,self.model.height//2
                                ,self.model.color,-90,90)
