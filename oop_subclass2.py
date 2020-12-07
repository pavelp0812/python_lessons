class Doctor:
    def __init__(self, degree):
        self.degree = degree
        print(" i'm a doctor")


class Builder:
    def __init__(self, rank):
        self.rank = rank
        print(" i'm a builder")


class Person(Doctor, Builder):

    def __init__(self, degree, rank):
        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f'{self.degree}, {self.rank}'


p = Person(3, 'qwe')
print(p)
