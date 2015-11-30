"""
1. Create a function that returns "ham"
2. Create a function that adds " sandwich" to all functions passed in
3. Apply decorator to first function
4. Repeat 1-3 for random float values
5. Continue being Awesome! :D
"""
import random


# 1
def return_ham(*args, **kwargs):
    return "ham"


# 2
def add_sandwich(func, *args, **kwargs):
    def add_sandwich_inside(*args, **kwargs):
        return func() + ' sandwich'

    return add_sandwich_inside


# 3
@add_sandwich
def return_new_ham(*args, **kwargs):
    return "NEW HAMM"


print return_new_ham()


# 4
# 4.1
def beer():
    return 5.32

print beer()

# 4.2
def multiply(func):
    def multiply_inside():
        return func() * random.randint(1, 100)

    return multiply_inside

# 4.3
@multiply
def beer():
    return 5.32

print beer()
