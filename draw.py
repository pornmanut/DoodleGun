import arcade

class Draw_Circle:
    def __init__(self,model):
        self.model = model

    def draw(self):
        arcade.draw_circle_filled(self.model.x,self.model.y,
                                    self.model.size,self.model.color)
class Draw_Rectangle:
    def __init__(self,model):
        self.model = model

    def draw(self):
        arcade.draw_rectangle_filled(self.model.x,self.model.y,
                                        self.model.width,self.model.height,
                                        self.model.color,self.model.angle)
