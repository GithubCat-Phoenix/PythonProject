class A:

    def __init__(self):
        self.name = "1"

    def __str__(self):
        return "%s" % self.name


class B(A):

    def __str__(self):
        return "%s" % self.name


m = B()
print(m)