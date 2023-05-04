from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("black")
        self.goto(-200, 200)
        self.write(f"Level : {self.level}", True, align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.goto(-200, 200)
        self.level += 1
        self.write(f"Level : {self.level}", True, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", True, align="center", font=FONT)
