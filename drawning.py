from turtle import Turtle

class Sxedio():

    def __init__(self):
        self.raketa1()
        self.raketa2()
        self.raketa3()
        self.raketa4()

    def raketa1(self):
        self.dokari1 = Turtle()
        self.dokari1.penup()
        self.dokari1.shape("square")
        self.dokari1.shapesize(stretch_wid=1, stretch_len=18)
        self.dokari1.color("white")
        self.dokari1.goto(0,70)

    def raketa2(self):
        self.dokari2 = Turtle()
        self.dokari2.penup()
        self.dokari2.shape("square")
        self.dokari2.shapesize(stretch_wid=1, stretch_len=18)
        self.dokari2.color("white")
        self.dokari2.goto(0,-70)


    def raketa3(self):
        self.dokari3 = Turtle()
        self.dokari3.penup()
        self.dokari3.shape("square")
        self.dokari3.shapesize(stretch_wid=18, stretch_len=1)
        self.dokari3.color("white")
        self.dokari3.goto(70,0)

    def raketa4(self):
        self.dokari4 = Turtle()
        self.dokari4.penup()
        self.dokari4.shape("square")
        self.dokari4.shapesize(stretch_wid=18, stretch_len=1)
        self.dokari4.color("white")
        self.dokari4.goto(-70, 0)
