from math import pi, sqrt


class Figure:

    def get_type(self):
        raise NotImplementedError()

    def get_sides(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()

    def get_area(self):
        raise NotImplementedError()


class NonNegative:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        assert value > 0,  'non-nagative value required'
        setattr(instance, self.name, value)


class Circle(Figure):
    type = 'Circle'
    r = NonNegative()

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


class Rectangle(Figure):
    type = 'Rectangle'
    a = NonNegative()
    b = NonNegative()


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


class Triangle(Figure):
    type = 'Triangle'
    a = NonNegative()
    b = NonNegative()
    c = NonNegative()


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def is_triangle_non_existent(self):
        self.res = self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a
        return self.res


    def get_type(self):
        return self.type


    def get_sides(self):
        if self.is_triangle_non_existent():
            return 'такого трикутника не існує'
        return f'a = {self.a}, b = {self.b}, c = {self.c}'


    def get_perimeter(self):
        if self.is_triangle_non_existent():
            return 'такого трикутника не існує'
        self.p = self.a + self.b + self.c
        return f'perimeter = {self.p}'


    def get_area(self):
        if self.is_triangle_non_existent():
            return 'такого трикутника не існує'
        self.pp = self.p / 2
        return f'area = {sqrt(self.pp * (self.pp - self.a) * (self.pp - self.b) * (self.pp - self.c))}'


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
