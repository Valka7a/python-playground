import turtle

# Get user's input
line_length = input('Enter length: ')
degree = input('Enter degree: ')

# Validate user's input
try:
    line_length = int(line_length)
    if line_length == 0:
        raise Exception('Length cannot be equal to 0.')

    degree = int(degree)

except ValueError:
    print('Invalid input!')
    exit()

except Exception as error:
    print(error)
    exit()

# Configure the turtle
turtle.speed('fastest')
turtle.color('green')

# Infinity Drawing
while True:
    turtle.right(degree)
    turtle.forward(line_length)