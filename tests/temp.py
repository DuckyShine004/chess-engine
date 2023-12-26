class A:
    def __init__(self):
        self.a = []


class B:
    def __init__(self, a):
        self.a = a
        self.b = self.a.a


foo = A()
bar = B(foo)
car = B(foo)

print(foo.a)

foo.a.append(1)

print(bar.b)
