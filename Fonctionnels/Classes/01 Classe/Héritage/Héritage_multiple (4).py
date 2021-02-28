print()

class X(object):
    def name(self):
        return 'I am an X'

class Y(object):
    def name(self):
        return 'I am an Y'

class Z(X, Y):
    xname = X.name
    yname = Y.name
    def name(self):
        return 'I am an Z, ie ' + self.xname() + ' and ' + self.yname()

for clss in [X, Y, Z]:
    obj = clss()
    print(obj.name())