import functools


def super_trace(func=None):
    if func is None:
        def deco(func):
            return super_trace(func)
        return deco


    @functools.wraps(func)
    def inner(*args, **kwargs):
        if ENABLE_TRACE:
            print(*[(type(i), i) for i in kwargs.values()])
            return func(*args, **kwargs)
    return inner


@super_trace()
def test4(a, b, *, c, d):
    print([a, b, c, d], a, str(b), float(c), d)


if __name__ == '__main__':

   ENABLE_TRACE = False
   test4(1, 2, c=3, d=4)


   ENABLE_TRACE = True
   test4(1, 2, c=3, d=4)


print('-' * 50)
print('так як додаткових аргументів не передається, можна написати коротшим 😎')


def deco(func):
    def inner(*args, **kwargs):
         if ENABLE_TRACE:
            print(*[(type(i), i) for i in kwargs.values()])
            return func(*args, **kwargs)
    return inner


@deco
def test4(a, b, *, c, d):
    print([a, b, c, d], a, str(b), float(c), d)


if __name__ == '__main__':

   ENABLE_TRACE = False
   test4(1, 2, c=3, d=4)


   ENABLE_TRACE = True
   test4(1, 2, c=3, d=4)