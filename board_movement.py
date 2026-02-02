UP=90
DOWN=270
from turtle import Turtle
class Board(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.penup()
        self.shape("square")
        self.resizemode("user")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinate)

    def move_up(self):
        cordinate=self.pos()
        self.goto(cordinate[0], cordinate[1]+20)
    def move_down(self):
        cordinate=self.pos()
        self.goto(cordinate[0], cordinate[1]-20)

