class Singleton(object):
    instance = None
    number = 0

    def __new__(self):
        self.number += 1
        if not self.instance:
            self.instance = super(Singleton, self).__new__(self)
        return self.instance


x = Singleton()
print x.number

x = Singleton()
print x.number

x = Singleton()
print x.number

x = Singleton()
print x.number

"""
def singleton(myclass):
    instances = {}
    def get_instance(*args, **kwargs):
        if myclass in instances:
            instances[myclass] = myclass(*args, **kwargs)
        return instances[myclass]

    return get_instance
"""

"""
_instance = None
def __new__(self):
    if not self._instance:
        self._instance = super(MySingleton, self).__new__(self)
        self.y = 10
    return self._instance

"""
