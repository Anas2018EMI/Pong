from re import S
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__( visible=False)
# visible=False
        self.color('white')
        self.penup()
        # self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.setpos(100,200)
        self.write(self.r_score, align='center', font=('Courier',60, 'normal'))

        self.setpos(-100,200)
        self.write(self.l_score, align='center', font=('Courier',60, 'normal'))

    def right_paddle_scores(self):
        self.r_score +=1
        self.update_score()

    def left_paddle_scores(self):
        self.l_score +=1
        self.update_score()

    


