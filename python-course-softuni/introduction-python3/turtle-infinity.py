import turtle

# Configure the turtle
turtle.speed('fast')
turtle.color('red')

# User input length and degrees
length = input('Enter length: ')
degrees = input('Enter degrees: ')

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
while (True):
    turtle.forward(length)
    turtle.left(degrees)
