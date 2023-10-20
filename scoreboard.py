from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 1
        self.penup()
        self.hideturtle()
        self.shapesize(2, 2)
        self.goto(0, 260)
        self.write(f"score: {self.score}", move=False, align='left', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align='left', font=('Arial', 12, 'normal'))

    def score_calculator(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score}", move=False, align='left', font=('Arial', 12, 'normal'))
