# any done


def my_any(object):
    for i in object:
        if i:
            return True
    return False


print('перевірка any')
print(any([True, False]) == my_any([True, False]))
print(any([True, True]) == my_any([True, True]))
print(any([False, False]) == my_any([False, False]))
print()


# all done
def my_all(object):
    for i in object:
        if not i:
            return False
    return True


print('перевірка all')
print(all([]) == my_all([]))
print(all([True, False]) == my_all([True, False]))
print(all([True, True]) == my_all([True, True]))
print(all([False, False]) == my_all([False, False]))
print()


# zip done
def your_zip(*object):
    res = []
    if len(object) == 1:
        for i in list(object[0]):
            res.append((i,))
        return res
    elif len(object) > 1:
        for i in range(min([len(i) for i in object])):
            res_p = []
            for j in range(len(object)):
                res_p.append(object[j][i])
            res.append(tuple(res_p))
        return res


print('перевірка zip')
print(list(zip(range(10), range(15), range(8))) == your_zip(range(10), range(15), range(8)))
print(list(zip(range(10), range(15), [])) == your_zip(range(10), range(15), []))
print(list(zip(range(10))) == your_zip(range(10)))
print()


# map done
def your_map(func, *obj):
    res = []
    if len(obj) > 1:
        for i in range(len(obj[0])):
            temp = []
            for j in obj:
                temp.append(j[i])
            res.append(func(temp))
    else:
        for i in obj[0]:
            res.append(func(i))
    return res


print('перевірка map')
print(list(map(int, '1234567890')) == your_map(int, '1234567890'))
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) ==
      your_map(min, range(10), range(20, 30), range(25, 15, -1)))
print()


#filter done

def your_filter(func, *obj):
    res = []
    if func is None:
        for i in obj[0]:
            if i:
                res.append(i)
    else:
        for i in obj[0]:
            if func(i):
                res.append(i)
    return res


print('перевірка filter')
print(list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == your_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]))
print(list(filter(lambda a: a % 2 == 0, range(10+1))) == your_filter(lambda a: a % 2 == 0, range(10+1)))
print()


# sum done
def your_sum(object):
    sum_object = 0
    for i in object:
        sum_object += i
    return sum_object


print('перевірка sum')
print(sum(range(10)) == your_sum(range(10)))
print(sum([]) == your_sum([]))
print()


# enumerate done
def your_enumerate(object, start = 0):

    res = []
    for i in object:
        res.append((start, i))
        start += 1
    return res


print('перевірка enumerate')
print(list(enumerate('1234567890', 1)) == your_enumerate('1234567890', 1))
print()


# range done
def your_range(*s):
    res, start, step = [], 0, 1
    if len(s) == 1:
        stop = s[0]
    elif len(s) == 2:
        start, stop = s
    else:
        start, stop, step = s
    if step > 0:
        while stop != start:
            if start > stop:
                break
            res.append(start)
            start += step
    if step < 0:
        while stop != start:
            if start < stop:
                break
            res.append(start)
            start += step
    return res


print('перевірка range')
print(list(range(10)) == your_range(10))
print(list(range(10, 20)) == your_range(10, 20))
print(list(range(10, 20, 3)) == your_range(10, 20, 3))
print(list(range(20, 10, 3)) == your_range(20, 10, 3))
print(list(range(20, 10, -3)) == your_range(20, 10, -3))
print(list(range(20, 10)) == your_range(20, 10))