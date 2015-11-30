def outside():
    x = 5
    def print_ham():
        print x
    return print_ham

myFunc = outside()
myFunc()


# other way
def outside(x = 5):
    def print_ham():
        print x
    return print_ham

myFunc = outside(7)
myFunc()
