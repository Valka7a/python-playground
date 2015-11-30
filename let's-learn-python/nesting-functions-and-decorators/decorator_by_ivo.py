def add_one(my_func):
    number = 1

    def add_one_inside():
        return my_func() + number

    return add_one_inside

def three_oranges():
    return 3

four_oranges = add_one(three_oranges)
print four_oranges()
five_oranges = add_one(four_oranges)
print five_oranges()
six_oranges  = add_one(five_oranges)
print six_oranges()
