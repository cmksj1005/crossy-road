from turtle import Turtle, Screen

SCORE_FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")
FINAL_SCORE_FONT = ("Courier", 30, "normal")

screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.level = 1

    def write_score(self):
        self.write(f"Level: {self.level}", align="center", font=SCORE_FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=SCORE_FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
