import turtle

# Configure the turtle
turtle.speed('slowest')
colors = ['red', 'blue', 'green', 'black']

# User input square length
square_size = input('Enter square length: ')

# Validate user input
try:
    square_size = int(square_size)

    if square_size == 0:
        raise Exception('Length cannot be equal to 0.')
except ValueError:
    print('Invalid input!')
    exit()
except Exception as error:
    print(error)
    exit()

# Draw square
for a in range(4):
    turtle.color(colors[a])
    turtle.forward(square_size)
    turtle.right(90)
