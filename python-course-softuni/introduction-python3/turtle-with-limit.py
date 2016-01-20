import turtle

# Configure the turtle
turtle.speed('fast')
turtle.color('red')

# User input length and degrees
length = input('Enter length: ')
degrees = input('Enter degrees: ')
interations = input('Enter interations: ')

try:
    length = int(length)
    degrees = int(degrees)
    interations = int(interations)

    if length == 0 or degrees == 0 or interations == 0:
        raise Exception('Length or degrees cannot be equal to 0.')
except ValueError:
    print('Invalid input!')
    exit()
except Exception as error:
    print(error)
    exit()


# Loop in range 1-100
number = 0
while number <= interations:
    turtle.forward(length)
    turtle.left(degrees)
    turtle.forward(length)
    turtle.right(number)
    turtle.forward(length)
    turtle.left(degrees + number)
    number += 1

turtle.exitonclick()
