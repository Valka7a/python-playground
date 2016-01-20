import turtle

# Get user square length from user
square_length = input('Enter square length: ')

# Validate user input
try:
    square_length = int(square_length)
    if square_length == 0:
        raise Exception('Length cannot be equal to 0.')

except ValueError:
    print('Invalid input!')
    exit()

except Exception as error:
    print(error)
    exit()

# Configure the turtle
turtle.speed('slow')
turtle.color('green')

# Draw square
for _ in range(4):
    turtle.forward(square_length)
    turtle.right(90)