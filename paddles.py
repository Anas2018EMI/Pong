from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cor_position):
        super().__init__(shape='square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.shapesize( stretch_len=1 ,stretch_wid=5)
        self.setpos(cor_position)

    def move_up(self):
        y_cor=self.ycor()
        if y_cor <250:
            self.sety(y_cor+20)
        else:
            self.sety(250)

    def move_down(self):
        y_cor=self.ycor()
        if y_cor>-250:
            self.sety(y_cor-20)
        else:
            self.sety(-250)