import turtle


# Generate one third side of the snowflake
def generate_side(side_length, iterations):
    if iterations == 0:
        turtle.forward(side_length)
        return

    side_length /= 3
    generate_side(side_length, iterations - 1)

    turtle.left(60)
    generate_side(side_length, iterations - 1)

    turtle.right(120)
    generate_side(side_length, iterations - 1)

    turtle.left(60)
    generate_side(side_length, iterations - 1)


# Generate Koch's Snowflake
def koch_snowflake(size, iterations):
    for _ in range(3):
        generate_side(size, iterations)
        turtle.right(120)


# Configure the turtle
turtle.speed('fastest')
turtle.bgcolor('lightblue')
turtle.color('white')

# Get user's input
snowflake_size = input('Enter snowflake size (500 is best): ')
iterations = input('Enter snowflake fractal iterations (4 is best): ')

# Validate user's input
try:
    snowflake_size = int(snowflake_size)
    if snowflake_size < 50:
        raise Exception('Length cannot be less then 50.')

    iterations = int(iterations)
    if iterations <= 0:
        raise Exception('Iterations cannot be less then or equal to 0.')

except ValueError:
    print('Invalid input!')
    exit()

except Exception as error:
    print(error)
    exit()

# Adjust turtle's initial position
turtle.penup()
turtle.backward(snowflake_size / 2)
turtle.pendown()

# Draw snowflake
koch_snowflake(snowflake_size, iterations)

# Wait for user's click to exit
turtle.exitonclick()