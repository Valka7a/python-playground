import turtle

# Configure the turtle
turtle.speed('slow')
turtle.color('red')

# User input length and degrees
length = input('How many is length a lines: ')
degrees = input('How many degrees wrap lines: ')

try:
    length = int(length)
    degrees = int(degrees)

    if length == 0 or degrees == 0:
        raise Exception('Length or degrees cannot be equal to 0.')
except ValueError:
    print('Invalid input!')
    exit()
except Exception as error:
    print(error)
    exit()


# Infinity loop
number = 1
while (True):
    turtle.forward(int(length))
    turtle.left(int(degrees))
    turtle.forward(int(length))
    turtle.right(number)
    turtle.forward(int(length))
    turtle.left(int(degrees) + number)
    number += 1
