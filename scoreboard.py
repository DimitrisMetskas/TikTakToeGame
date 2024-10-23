from turtle import Turtle
import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(0, 250)
        self.write("That's a Game Over", align="center", font=("Courier", 40, "normal"))

    def wehaveawinner(self, winner):
        self.goto(0, 250)
        self.write(f"{winner} Won!", align="center", font=("Courier", 40, "normal"))
        return False


    def startingmessage(self):
        self.goto(0, 250)
        self.write(" You are the Blue Circle. Computer is the Red Turtle! \n When the Blue Circle Apear you have 2 second to make a choice (approx), \n where you want to put it! Good Luck!", align="center", font=("Courier", 15, "normal"))
        time.sleep(5)
        self.clear()

