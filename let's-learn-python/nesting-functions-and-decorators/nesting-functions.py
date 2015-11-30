def outside():
    def print_ham():
        print 'ham'
    return print_ham


myFunc = outside()
myFunc()
