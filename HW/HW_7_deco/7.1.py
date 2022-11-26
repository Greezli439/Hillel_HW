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
            print(len(args), file=file)
            return func(*args, **kwargs)
    return inner


@super_trace(file=sys.stderr)
def test1(a, b, c):
    return [a, b, c], a, str(b), float(c)


if __name__ == '__main__':

   ENABLE_TRACE = False
   test1(1, 2, 3)


   ENABLE_TRACE = True
   test1(1, 2, 3)
