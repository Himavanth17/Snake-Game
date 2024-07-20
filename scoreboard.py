from turtle import Turtle

with open("high_score.txt") as file:
    contents = file.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(contents)
        self.penup()
        self.hideturtle()
        self.setposition(0,280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.score} high score {self.high_score}")


    #def game_over(self):
        #self.goto(0,0)


    def score_add(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()




