class BaseClass(object):
    def test(self):
        print "ham"

class InClass(BaseClass):
    def test(self):
        print "hammer time"

i = InClass()
i.test()
