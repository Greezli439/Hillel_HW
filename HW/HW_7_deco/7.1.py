import sys
import functools


def super_trace(func=None, *, file=sys.stdout):
    if func is None:
        def deco(func):
            return super_trace(func, file=file)
        return deco


    @functools.wraps(func)
    def inner(*args, **kwargs):
        if ENABLE_TRACE:
            print(file=file)
            print(func.__name__, file=file)
            if args:
                print(f'Кількість вхідних позиційних аргументів декоруємої функції = {len(args)}', file=file)
                print(f'Тип і значення кожного позиційного аргументу декоруємої функції ->', end = ' ', file=file)
                print(*[(type(i), i) for i in args], file=file)
            if kwargs:
                print(f'Кількість вхідних іменованих аргументів декоруємої функції = {len(kwargs)}', file=file)
                print(f'Тип і значення кожного іменованого аргументу декоруємої функції ->', end=' ', file=file)
                print(*[(type(i), i) for i in kwargs.values()], file=file)
            res_func = func(*args, **kwargs)
            if res_func:
                print('Кількість аргументів, що повертає функція =', len(res_func), file=file)
                print(f'Кількість, тип та значення що повертає декорована функція =>', end=' ', file=file)
                print(*[(type(i), i) for i in res_func], file=file)
        return func(*args, **kwargs)
    return inner



@super_trace(file=sys.stderr)
def test1(a, b, c):
    return [a, b, c], a, str(b), float(c)


@super_trace()
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d


@super_trace(file=sys.stderr)
def test3(*, a, b, c, d):
    return [a, b, c, d], a, str(b), float(c), d


@super_trace()
def test4(a, b, *, c, d):
    print([a, b, c, d], a, str(b), float(c), d)


@super_trace()
def test5():
    return [1, 2, 3]


if __name__ == '__main__':
    # test ENABLE_TRACE = False
    ENABLE_TRACE = False
    test1(1, 2, 3)
    test2(1, 2, c=3, d=4)
    test3(a=1, b=2, c=3, d=4)
    test4(1, 2, c=3, d=4)
    test5()

    # test ENABLE_TRACE = True
    ENABLE_TRACE = True
    test1(1, 2, 3)
    test2(1, 2, c=3, d=4)
    test3(a=1, b=2, c=3, d=4)
    test4(1, 2, c=3, d=4)
    test5()
