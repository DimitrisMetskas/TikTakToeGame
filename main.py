from turtle import Screen
import time
from drawning import Sxedio
from game import Kiklos, Xi
import gunicorn

screen = Screen()
screen.setup(width=900, height=700)

screen.bgcolor("black")
screen.title("Tik Tak Toe")

sxedio = Sxedio()
kiklos = Kiklos()
xi = Xi()

kiklos.startingmessage()

keep_on = True
a = True
while keep_on:
    kiklos.turn()
    if not kiklos.check():
        keep_on = False
        winner = "You"
        a = kiklos.wehaveawinner(winner)

    if a:
        time.sleep(0.5)
        xi.turn()
        if xi.check() == False:
            winner = "Computer"
            keep_on = False
            xi.wehaveawinner(winner)

screen.exitonclick()
