import turtle

# Get user's input
iterations = input('Enter iterations: ')

# Validate user's input
try:
    iterations = int(iterations)
    if iterations <= 0:
        raise Exception('Length cannot be less then or equal to 0.')

except ValueError:
    print('Invalid input!')
    exit()

except Exception as error:
    print(error)
    exit()

# Drawing for x iterations
degree = 134
length = 120
current_iterations = 0

while current_iterations < iterations:
    turtle.left(degree)
    turtle.forward(length)
    current_iterations += 1

turtle.exitonclick()