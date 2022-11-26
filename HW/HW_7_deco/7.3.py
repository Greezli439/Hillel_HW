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
            print(len(kwargs), file=file)
            return func(*args, **kwargs)
    return inner


@super_trace(file=sys.stderr)
def test3(*, a, b, c, d):
    return [a, b, c, d], a, str(b), float(c), d


if __name__ == '__main__':

   ENABLE_TRACE = False
   test3(a=1, b=2, c=3, d=4)


   ENABLE_TRACE = True
   test3(a=1, b=2, c=3, d=4)
