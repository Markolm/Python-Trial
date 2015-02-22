from turtle import *
import random

pen = Pen()
bgcolor("black")
size = 5
color = ["blue","red","green","yellow","cyan","orange","pink","purple","lime"]
pen.speed(0)
for a in range(500):
    pen.color(random.choice(color))
    pen.forward(size)
    pen.left(170)
    size = size+1
