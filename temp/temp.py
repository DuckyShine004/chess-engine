class A:
    def __init__(self):
        self.a = [1, 2, 3]


class B:
    def __init__(self, a):
        self.a = a.a


a = A()
b = B(a)

print(a.a)
b.a.append(1)

print(a.a)
