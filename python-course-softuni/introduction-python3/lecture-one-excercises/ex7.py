import turtle

# Get user's input
board_size = input('Enter bord size: ')

# Validate user's input
try:
    board_size = int(board_size)
    if board_size < 8:
        raise Exception('Board size cannot be less then 8.')

except ValueError:
    print('Invalid input!')
    exit()

except Exception as error:
    print(error)
    exit()


# Configure turtle's color based on current row and col
def configure_turtle_color(row, col):
    if row % 2 == 1:
        col += 1

    if col % 2 == 0:
        turtle.color('black')
        return

    turtle.color('white')


# Draw single square with the size provided
def draw_square(size, fill=True):
    if fill:
        turtle.begin_fill()

    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

    if fill:
        turtle.end_fill()


# Draw borders around the board,
# so it can be seen properly with
# any background color
def draw_board_borders():
    turtle.penup()
    turtle.color('black')
    turtle.goto(-1, -1)
    turtle.pendown()

    draw_square(board_size + 2, False)

    turtle.penup()
    turtle.color('white')
    turtle.goto(-2, -2)
    turtle.pendown()

    draw_square(board_size + 4, False)


# Draw the chess board
def draw_chess_board():
    item_length = board_size / 8
    row = x_coord = y_coord = 0

    for number in range(1, 65):
        configure_turtle_color(row, number)

        turtle.penup()
        turtle.goto(x_coord, y_coord)
        turtle.pendown()

        draw_square(item_length)

        x_coord += item_length

        if number % 8 == 0:
            row += 1
            x_coord = 0
            y_coord += item_length

    draw_board_borders()


# Configure the turtle
turtle.speed('fastest')
turtle.bgcolor('brown')

# Draw
draw_chess_board()

# Move the turtle to the side,
# so the chessboard is seen
# better when it's with smaller size
turtle.penup()
turtle.goto(-10, -10)

# Wait for user's click to exit
turtle.exitonclick()