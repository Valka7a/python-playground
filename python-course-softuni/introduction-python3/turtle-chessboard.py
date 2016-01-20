import turtle

turtle.speed('fastest')
turtle.bgcolor('white')
length = 40
number = 1
line = 0
for row in range(64):

    if row % 8 == 0:
        line += 1
        number = 1

    if line % 2 == 0:
        if row % 2 == 0:
            turtle.color('black')
        else:
            turtle.color('white')
    else:
        if row % 2 == 1:
            turtle.color('black')
        else:
            turtle.color('white')

    turtle.penup()
    turtle.goto((number * length) - length, (line - 1) * length)
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(length)
        turtle.left(90)

    turtle.end_fill()
    number += 1

turtle.penup()
turtle.goto(-1, -1)
turtle.pendown()
turtle.color('white')
for _ in range(4):
    turtle.forward(322)
    turtle.left(90)


turtle.penup()
turtle.goto(-2, -2)
turtle.pendown()
turtle.color('black')
for _ in range(4):
    turtle.forward(324)
    turtle.left(90)

turtle.exitonclick()
