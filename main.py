from turtle import Turtle, Screen, Pen
import random
from random import choice
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 234), (222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.penup()
timmy.goto(-200,-200)
print(timmy)
timmy.pendown()
def dot():
    for _ in range(14):
        clr = random.choice(color_list)
        timmy.dot(20,clr)
        timmy.penup()
        timmy.forward(35)
dot()
timmy.left(90)
timmy.forward(35)
timmy.left(90)
dot()
timmy.right(90)
timmy.forward(35)
timmy.right(90)

def move():
    dot()
    timmy.left(90)
    timmy.forward(35)
    timmy.left(90)
    dot()
    timmy.right(90)
    timmy.forward(35)
    timmy.right(90)
for _ in range(6):
    move()

timmy.shape('turtle')
timmy.color("green")

screen.exitonclick()
