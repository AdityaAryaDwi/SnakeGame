from turtle import Turtle
FONT=("Courier",16,"normal")
#nfile=open("data.txt")
#temp=nfile.read()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as nfile:
            self.high_score=int(nfile.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=280)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}",False,"center",FONT)

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt","w") as nfile:
                nfile.write(str(self.high_score))
        self.score=0
        self.update_scoreboard()

    def refresh(self):
        self.score+=1
        self.update_scoreboard()