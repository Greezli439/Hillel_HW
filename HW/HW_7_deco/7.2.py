import functools


def super_trace(func=None):
    if func is None:
        def deco(func):
            return super_trace(func)
        return deco


    @functools.wraps(func)
    def inner(*args, **kwargs):
        if ENABLE_TRACE:
            print(*[(type(i), i) for i in args])
            return func(*args, **kwargs)
    return inner


@super_trace()
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d

if __name__ == '__main__':

   ENABLE_TRACE = False
   test2(1, 2, c=3, d=4)

   ENABLE_TRACE = True
   test2(1, 2, c=3, d=4)


print('-' * 50)
print('так як додаткових аргументів не передається, можна написати коротшим 😎')


def deco(func):
    def inner(*args, **kwargs):
        if ENABLE_TRACE:
            print(*[(type(i), i) for i in args])
    return inner


@deco
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d

if __name__ == '__main__':

   ENABLE_TRACE = False
   test2(1, 2, c=3, d=4)

   ENABLE_TRACE = True
   test2(1, 2, c=3, d=4)

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
