class BaseClass(object):
    def test(self):
        print "ham"

class InClass(BaseClass):
    def test(self):
        print "hammer time"

print BaseClass.__subclasses__()
