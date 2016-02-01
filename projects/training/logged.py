"""
class logged:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('you called {.__name__}({}{}{})'.format(
            func,
            str(list(args))[1: -1], # cast to list is because tuple
                                    # of length one has an extra comma
            ', ' if kwargs else '',
            '. '.join('{}={}'.format(*pair) for pair in kwargs.items()),
            ))
        val = func(4, 4, 4)
        print ('it returned', val)
        return val

"""

def logged(func):
    """Print out the arguments before function call and
    after the call print out the returned value
    """
    def wrapper(*args, **kwargs):
        print('you called {.__name__}({}{}{})'.format(
            func,
            str(list(args))[1:-1],  # cast to list is because tuple
                                    # of length one has an extra comma
            ', ' if kwargs else '',
            ', '.join('{}={}'.format(*pair) for pair in kwargs.items()),
            ))
        val = func(*args, **kwargs)
        print('it returned', val)
        return val
    return wrapper
