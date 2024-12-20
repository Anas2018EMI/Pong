from re import S
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        # shape='circle'
        self.color('white')
        self.setpos((0,0))
        self.penup()
        self.setheading(36)
        self.forward_pace=5

   
    def detect_collision_with_walls(self)   :
        if self.ycor()>= 290 or self.ycor()<=-290 :
            self.setheading(-self.heading())
        

    def move(self)   :
        self.detect_collision_with_walls()
        self.forward(self.forward_pace)

    def check_missed_balls(self):
        if self.xcor() > 380 :
            self.setpos((0,0))
            self.forward_pace=5
            self.setheading(36+90)
            return 'left'
        elif self.xcor() < -380:
            self.setpos((0,0))
            self.forward_pace=5
            self.setheading(36)
            return 'right'
       
 
# self.setheading(36.5)
# self.forward(5)

# x_cor=self.xcor() +10
# y_cor=self.ycor() +10
# self.setpos(x_cor, y_cor)
#if self.ycor()>= 200 or self.ycor()<=-200:
# if self.distance((self.xcor(), 200))< 5:
# print(f" angle: {self.heading()} ; x_cor {x_cor}; y_cor: {y_cor}")


    # def move_to_top_right(self):
    #     x_cor=self.xcor() +10
    #     y_cor=self.ycor() +10
    #     self.setpos(x_cor, y_cor)