from turtle import Screen, Turtle
import random
from scoreboard import Scoreboard
import time
import numpy as np

THESIS = [[0, 110],
          [110, 110],
          [110, 0],
          [110, -110],
          [0, -110],
          [-110, -110],
          [-110, 0],
          [-110, 110],
          [0, 0]
          ]

NIKI = [
    [[-110, 110], [0, 110], [110, 110]],
    [[-110, 0], [0, 0], [110, 0]],
    [[-110, -110], [0, -110], [110, -110]],
    [[-110, 110], [-110, 0], [-110, -110]],
    [[0, 110], [0, 0], [0, -110]],
    [[110, 110], [110, 0], [110, -110]],
    [[-110, 110], [0, 0], [110, -110]],
    [[-110, -110], [0, 0], [110, 110]]
]
screen = Screen()
screen.listen()


class Kiklos(Scoreboard):

    def __init__(self):
        super().__init__()
        self.poss = []

    def turn(self):
        try:
            mini = 11110
            pos_min = (0, 0)
            # for starting not in the center!
            simataki = Turtle(shape="circle", visible=False)
            simataki.penup()
            simataki.goto(-300, 20)
            # simataki.pendown()
            simataki.color("blue")
            simataki.showturtle()

            screen.onclick(simataki.goto)
            time.sleep(2)
            screen.update()
            pos = simataki.position()

            for x in THESIS:
                point1 = np.array(x)
                point2 = np.array(pos)
                dist = np.linalg.norm(point1 - point2)

                if dist < mini:
                    mini = dist
                    pos_min = x

            simataki.goto(pos_min)
            # time.sleep(1)
            THESIS.remove(pos_min)
            self.poss.append(pos_min)
        except IndexError:
            while True:
                self.update_scoreboard()

    def check(self):
        keep_on = True
        for x in self.poss:
            for k in range(0, len(NIKI)):
                point = 0
                for o in NIKI[k]:
                    if x == o:
                        point += 1
                        if point == 1:
                            arithmoi = 0
                            for z in self.poss:
                                for a in NIKI[k]:
                                    if z == a:
                                        arithmoi += 1
                                        if arithmoi == 3:
                                            keep_on = False
        return keep_on



class Xi(Scoreboard):

    def __init__(self):
        super().__init__()
        self.poss = []

    def turn(self):
        try:
            a = random.choice(THESIS)
            simataki = Turtle()
            simataki.penup()
            simataki.shape("turtle")
            simataki.color("red")
            simataki.goto(a)
            THESIS.remove(a)
            self.poss.append([simataki.xcor(), simataki.ycor()])
        except IndexError:
            while True:
                self.update_scoreboard()

    def check(self):
        keep_on = True
        for x in self.poss:
            for k in range(0, len(NIKI)):
                point = 0
                for o in NIKI[k]:
                    if x == o:
                        point += 1
                        if point == 1:
                            arithmoi = 0
                            for z in self.poss:
                                for a in NIKI[k]:
                                    if z == a:
                                        arithmoi += 1
                                        if arithmoi == 3:
                                            keep_on = False
        return keep_on

