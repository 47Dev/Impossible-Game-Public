import turtle as t
import random as r

x = r.randrange(-280, 300, 15)
y = r.randrange(-290, 290, 15)

screen = t.Screen()
screen.bgcolor('blue')
screen.title("Impossible Game")

sq = t.Turtle()
sq.pencolor('black')
sq.pensize(5)
sq.penup()
sq.speed(0)
sq.goto(-400, -300)
sq.pendown()
sq.setposition(400, -300)
sq.setposition(400, 300)
sq.setposition(-400, 300)
sq.setposition(-400, -300)
sq.hideturtle()

# Player
pl = t.Turtle()
pl.shape("square")
pl.color('black')
pl.penup()
pl.shapesize(stretch_wid=1.44, stretch_len=1.44)
pl.speed(0)
pl.goto(290, 0)

plspeed = 15

# Obstacle, AI
en = t.Turtle()
en.shape("square")
en.color('white')
en.penup()
en.shapesize(stretch_wid=6, stretch_len=1.33)
en.speed(0)
en.goto(-290, 0)

# The End of  level
end = t.Turtle()
end.penup()
end.speed(0)
end.shape('square')
end.goto(-350, 0)
end.shapesize(stretch_wid=8, stretch_len=4)
end.color('red')

#text

pen = t.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(310, 0)


def up():
    y = pl.ycor()
    y += plspeed
    if y > 300:
        y = 290
    pl.sety(y)
    print('x: ', pl.xcor(), 'y: ', pl.ycor())


screen.listen()
screen.onkeypress(up, 'Up')


def down():
    y = pl.ycor()
    y -= plspeed
    if y < -300:
        y = -290
    pl.sety(y)
    print('x: ', pl.xcor(), 'y: ', pl.ycor())


screen.listen()
screen.onkeypress(down, 'Down')


def Right():
    x = pl.xcor()
    x += plspeed
    if x > 400:
        x = 390
    pl.setx(x)
    print('x: ', pl.xcor(), 'y: ', pl.ycor())


screen.listen()
screen.onkeypress(Right, 'Right')


def Left():
    x = pl.xcor()
    x -= plspeed
    if x < -280:
        x = -265
    pl.setx(x)
    print('x: ', pl.xcor(), 'y: ', pl.ycor())


screen.listen()
screen.onkeypress(Left, 'Left')

while True:
    screen.update()


    def AIMov():
        y = pl.ycor()
        en.sety(y)


    AIMov()
    

pl.goto(-360, 300)

def pl2():
    pl2 = t.Turtle()
    pl2.shape("square")
    pl2.color('black')
    pl2.penup()
    pl2.shapesize(stretch_wid=1.44, stretch_len=1.44)
    pl2.speed(0)
    pl2.goto(290, 0)

    def up():
        y = pl2.ycor()
        y += plspeed
        if y > 300:
            y = 290
        pl2.sety(y)
        print('x: ', pl.xcor(), 'y: ', pl.ycor())


    screen.listen()
    screen.onkeypress(up, 'Up')


    def down():
        y = pl2.ycor()
        y -= plspeed
        if y < -300:
            y = -290
        pl2.sety(y)
        print('x: ', pl.xcor(), 'y: ', pl.ycor())


    screen.listen()
    screen.onkeypress(down, 'Down')


    def Right():
        x = pl2.xcor()
        x += plspeed
        if x > 400:
            x = 390
        pl2.setx(x)
        print('x: ', pl.xcor(), 'y: ', pl.ycor())


    screen.listen()
    screen.onkeypress(Right, 'Right')

    def Left():
        x = pl2.xcor()
        x -= plspeed
        if x < -280:
            x = -265
        pl2.setx(x)
        print('x: ', pl.xcor(), 'y: ', pl.ycor())


    screen.listen()
    screen.onkeypress(Left, 'Left')



while True:
    screen.update()
    if pl.xcor() > -360 and pl.ycor() <= 0:
        pl.hideturtle()
        screen.bgcolor('red')
        pl.color('blue')

        pl.goto(-290, 0)

        en.hideturtle()

    print('X: ', pl.xcor(),'y: ', pl.ycor())
