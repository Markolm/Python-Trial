from turtle import *
import random
pen = Pen()
pen.screen.bgcolor("#43AD96")

pen.color("#000000")

pen.begin_fill()

pen.up()
pen.goto(-300, 300)
pen.down()
pen.goto(-300, 100)
pen.goto(-100, 100)
pen.goto(-100, 300)
pen.goto(-300, 300)

pen.end_fill()
pen.begin_fill()

pen.up()
pen.goto(300, 300)
pen.down()
pen.goto(300, 100)
pen.goto(100, 100)
pen.goto(100, 300)
pen.goto(300, 300)

pen.end_fill()
pen.begin_fill()

pen.up()
pen.goto(-100, 100)
pen.down()
pen.goto(100, 100)
pen.goto(100, -200)
pen.goto(-100, -200)
pen.goto(-100, 100)

pen.end_fill()
pen.begin_fill()

pen.up()
pen.goto(-100, 0)
pen.down()
pen.goto(-200, 0)
pen.goto(-200, -300)
pen.goto(-100, -300)
pen.goto(-100, 0)

pen.end_fill()
pen.begin_fill()

pen.up()
pen.goto(100, 0)
pen.down()
pen.goto(200, 0)
pen.goto(200, -300)
pen.goto(100, -300)
pen.goto(100, 0)

pen.end_fill()

