import functools
import sys


def super_trace(func=None, *, file=sys.stdout):
    if func is None:
        def deco(func):
            return super_trace(func, file=file)
        return deco


    @functools.wraps(func)
    def inner(*args, **kwargs):
        if ENABLE_TRACE:
            print('Кількість аргументів, що повертає функція =', len(func()))
            print(*[(type(i), i) for i in func()])
            return func(*args, **kwargs)
    return inner


@super_trace()
def test5():
    return [1, 2, 3]


if __name__ == '__main__':
   ENABLE_TRACE = False
   test5()
   ENABLE_TRACE = True
   test5()


print('-' * 50)
print('так як додаткових аргументів не передається, можна написати коротшим 😎')


def deco(func):
    def inner():
        if ENABLE_TRACE:
            print('Кількість аргументів, що повертає функція =', len(func()))
            print(*[(type(i), i) for i in func()])
    return inner


@deco
def test5():
    return [1, 2, 3]


if __name__ == '__main__':
   ENABLE_TRACE = False
   test5()
   ENABLE_TRACE = True
   test5()

   print('Кількість аргументів, що повертає функція =', len(func()))
   print(f'Кількість, тип та значення що повертає декорована функція =>', end=' ', file=file)
   print(*[(type(i), i) for i in func()])