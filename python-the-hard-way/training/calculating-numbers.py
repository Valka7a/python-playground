import sys


def sum_list(lists, acc = 0):
    if lists:
        acc += lists.pop()
        return sum_list(lists, acc)
    return acc



def min_list(lists, acc = int(sys.maxsize)):
    if lists:
        a = lists.pop()
        return min_list(lists, a if a < acc else acc)
    return acc


def max_list(lists, acc = int(-sys.maxsize)):
    if lists:
        a = lists.pop()
        return max_list(lists, a if a > acc else acc)
    return acc

def avg(lists, summ = 0, count = 0):
    if lists:
        return avg(lists, summ + lists.pop(), count + 1)
    return summ / count


numbers = [1, 2, 3, 4, 5]
print "Min:", min_list(numbers)
numbers = [1, 2, 3, 4, 5]
print "Max:", max_list(numbers)
numbers = [1, 2, 3, 4, 5]
print "Sum:", sum_list(numbers)
numbers = [1, 2, 3, 4, 5]
print "Avg:", avg(numbers)
"""
The way it works

sum_list([1, 2, 3, 4, 5], 0)
sum_list([1, 2, 3, 4], 5)
sum_list([1, 2, 3], 9)
sum_list([1, 2], 12)
sum_list([1], 14)
sum_list([], 15)

else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
"""




sum (List) ->
  sum(List, 0).

sum ([], Sum) ->
  Sum.
sum ([Head | Tail], Sum) ->
  sum(Tail, Sum + Head).
