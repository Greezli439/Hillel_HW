from math import pi, sqrt

class Circle:
    type = 'Circle'


    def __init__(self, args):
        self.r = args


    def get_type(self):
        return self.type


    def get_sides(self):
        return f'r = {self.r}'


    def get_perimeter(self):
        return f'perimeter = {2 * pi * self.r}'


    def get_area(self):
        return f'area = {pi * self.r ** 2}'



class Rectangle:
    type = 'Rectangle'


    def __init__(self, a, b):
        self.a = a
        self.b = b


    def get_type(self):
        return self.type


    def get_sides(self):
        return f'a = {self.a}, b = {self.b}'


    def get_perimeter(self):
        return f'perimeter = {(self.a + self.b) * 2}'


    def get_area(self):
        return f'area = {self.a * self.b}'


class Triangle:
    type = 'Triangle'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def get_type(self):
        return self.type


    def get_sides(self):
        return f'a = {self.a}, b = {self.b}, c = {self.c}'


    def get_perimeter(self):
        global p
        p = self.a + self.b + self.c
        return f'perimeter = {p}'


    def get_area(self):
        pp = p / 2
        return f'area = {sqrt(pp * (pp - self.a) * (pp - self.b) * (pp - self.c))}'


def get_class(raw_input):
    args = raw_input.split()
    count = len(args)
    if count == 1:
        r = int(raw_input)
        if r <= 0:
            print('такого кола не існує')
        else:
            return Circle(r)
    elif count == 2:
        a, b = [int(i) for i in args]
        if a <= 0 or b <= 0:
            print('такого чотирикутника не існує')
        else:
            return Rectangle(a, b)
    elif count == 3:
        a, b, c = [int(i) for i in args]
        if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
            print('такого трикутника не існує')
        else:
            return Triangle(a, b, c)
    else:
        return None


if __name__ == '__main__':
    raw_input = input()
    object = get_class(raw_input)
    if object:
        print(object.get_type())
        print(object.get_sides())
        print(object.get_perimeter())
        print(object.get_area())

