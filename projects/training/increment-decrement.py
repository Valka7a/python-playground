numbers = [1, 2, 3, 4, 5]

def increment_list_values(list):
    return map(lambda item: item + 1, list)

print increment_list_values(numbers)


def decrement_list_value(list):
    return map(lambda item: item - 1, list)

print decrement_list_value(numbers)


def multiplication_list_value(list):
    return map(lambda item: item * item, list)

print multiplication_list_value(numbers)


def even_number_list_value(list):
    return filter(lambda item: item % 2 == 0, list)

print even_number_list_value(numbers)


def even_number_list_value_multiplicated(list):
    even = filter(lambda item: item % 2 == 0, list)
    return map(lambda item: item * 2, even)

print even_number_list_value_multiplicated(numbers)
