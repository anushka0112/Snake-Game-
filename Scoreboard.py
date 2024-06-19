from turtle import Turtle
alignment="center"
font=("Arial", 24, "normal")
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score: {self.highscore}", False, alignment, font)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",False,alignment,font)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt","w")as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()