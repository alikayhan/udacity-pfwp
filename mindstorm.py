__author__ = 'alikayhan'

import turtle
import time
import twilio

window = turtle.Screen()
window.bgcolor("yellow")

def draw_square():
    husnu = turtle.Turtle("arrow")
    husnu.color("red")
    husnu.speed(1)

    for i in range(0, 4):
        husnu.forward(100)
        husnu.right(90)

def draw_circle():
    zekiye = turtle.Turtle("arrow")
    zekiye.color("blue")
    zekiye.speed(1)

    zekiye.circle(50)


def draw_triangle():
    maho = turtle.Turtle("turtle")
    maho.color("green")
    maho.speed(2)

    for i in range(0, 3):
        maho.forward(200)
        maho.left(120)

print(twilio.__version__)
draw_square()
draw_circle()
draw_triangle()
time.sleep(10)

