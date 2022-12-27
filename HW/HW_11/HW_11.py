def your_zip(*object):
    for i in range(min([len(i) for i in object])):
        yield
        res = []
        for j in range(len(object)):
            res.append(object[j][i])
        print(tuple(res))


def your_map(func, *obj):
    if len(obj) > 1:
        for i in range(len(obj[0])):
            yield
            temp = []
            for j in obj:
                temp.append(j[i])
            print(func(temp))
    else:
        for i in obj[0]:
            yield
            print(func(i))


def your_filter(func, *obj):
    if func is None:
        for j in obj:
            for i in j:
                if i:
                    yield
                    print(i)
    else:
        for j in obj:
            for i in j:
                if func(i):
                    yield
                    print(i)


def your_enumerate(object, start = 0):
    for i in object:
        print((start, i))
        start += 1
        yield


def your_range(*s):
    start, step = 0, 1
    if len(s) == 1:
        stop = s[0]
    elif len(s) == 2:
        start, stop = s
    else:
        start, stop, step = s
    if step > 0:
        while stop != start:
            yield
            if start > stop:
                break
            print(start)
            start += step
    if step < 0:
        while stop != start:
            yield
            if start < stop:
                break
            print(start)
            start += step
    return 'generator was completed.'

