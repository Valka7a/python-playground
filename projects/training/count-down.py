def count_down_counter(numbers):
    all_numbers = []
    for number in range(numbers, -1, -1):
        all_numbers.append(number)
    return all_numbers

wat = count_down_counter(10)
print wat

def count_d_counter(numbers):
    all_numbers = []
    while numbers > 0:
        all_numbers.append(numbers)
        numbers -= 1
    else:
        all_numbers.append("BaNG!")

    return all_numbers

print count_d_counter(10)



def c_down_counter(numbers):

    while numbers > 0:
        print numbers
        numbers -= 1

    print "BaNG!"

c_down_counter(10)

def count_down_c(number):
    if number >= 1:
        print number
        return count_down_c(number - 1)

    print "BaNG!"

count_down_c(10)
