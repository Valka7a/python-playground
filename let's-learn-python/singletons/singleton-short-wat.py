# If exists return the same, if not create new
def singleton(myclass):
    instances = {}
    def get_instance(*args, **kwargs):
        if myclass not in instances:
            instances[myclass] = myclass(*args, **kwargs)
        return instances[myclass]

    return get_instance

@singleton
class TestClass(object):
    pass

x = TestClass()

print x
a = TestClass()

print a
@singleton
class TestClassB(object):
    pass


b = TestClassB()
print b

c = TestClassB()
print c
