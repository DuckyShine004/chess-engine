class A:
    def __init__(self):
        self.a = [1, 2, 4]
        self.b = 1
        self.c = self.b

        self.b += 1

        print(self.c)

    def get_list(self):
        return [a for a in self.a]


foo = A()

print(foo.a)
b = foo.get_list()
b.append(3)

print(foo.a, b)
