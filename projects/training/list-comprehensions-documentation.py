"""
List comprehensions provide a concise way to lists. Common applications are to
make new lists where each element is the result of some operations applied to
each member of another sequence or iterable, or to create a subsequence of those
elements that satisfy a certain condition.

--------------------------------------------------------------------------------
For example, assume we want to create a list of squares, like:
>>> squares = []
>>> for x in range(10):
...     squares.append(x ** 2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
--------------------------------------------------------------------------------
We can obtain the same result with:
squares = [x ** 2 for x in range(10)]
--------------------------------------------------------------------------------
This is alose equivalent to:
squares = map(lambda x: x ** 2, range(10))
But it's more concise and readable.
--------------------------------------------------------------------------------
A list comprehension consists of brackets containing an expression followed by a
'for' clause, then zero or more 'for' or 'if' clauses. The result will be a new
list resulting from evaluating the expression in the context of the 'for' and
'if' clauses which follow it. For example, this listcomp combines the elements
of two lists if they are not equal:
>>> [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
________________________________________________________________________________
And it's equivalent to:
>>> combs = []
>>> for x in [1, 2, 3]:
...     for y in [3, 1, 4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

Note how the order of the 'for and 'if' statements is the same in both these
snippets.
________________________________________________________________________________
If the expression is a tuple (e.g. the (x, y) in the previous example), it must
be parenthesized.
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x * 2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruits = ['  banana', '  loganberry', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x ** 2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x ** 2 for x in range(6)]
file "<stdin>", line 1
    [x, x ** 2 for x in range(6)]

SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with tow 'for'
>>> vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
________________________________________________________________________________
List comprehensions can contain complex expressions and nested functions:
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
________________________________________________________________________________
