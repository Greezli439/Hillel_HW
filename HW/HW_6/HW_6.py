#set
print('set')
#1
print('ex_1')
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}
res1 = set_a | set_b | set_c
print(f'{res1=}')
print()

#2
print('ex_2')
res_a_b = set_a - set_b
res_b_c = set_b - set_c
res_a_c = set_a - set_c
print(f'{res_a_b=}')
print(f'{res_b_c=}')
print(f'{res_a_c=}')
print()

#3
print('ex_3')
res_a_b = set_a & set_b
res_b_c = set_c & set_b
res_a_c = set_a & set_c
print(f'{res_a_b=}')
print(f'{res_b_c=}')
print(f'{res_a_c=}')
print()

#4
print('ex_4')
print({1,2}.issubset(set_a))
print({1,2}.issubset(set_b))
print({1,2}.issubset(set_c))
print()

#5
print('ex_5')
res_1, res_2 = set(), set()
for i in res1:
    if i % 2 == 0:
        res_1.add(i)
    else:
        res_2.add(i)
print(f'{res_1=}')
print(f'{res_2=}')
print()

#Dict
print('Dict')
#ex_1
print('ex_1')
dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}

dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}

dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}
res_1 = dict_a.copy()
res_1.update(dict_b)
print(f'{res_1=}')
print()

#2
print('ex_2')
res = dict(zip(dict_a.keys(), dict_b.values()))
print(f'{res=}')
print()

#3
print('ex_3')
res = dict(zip(dict_b.keys(), dict_a.values()))
print(f'{res=}')
print()

#4
print('ex_4')
res = {}
for keys_d, values_d in res_1.items():
    if int(keys_d[-1]) % 2 == 1 and int(values_d[-1]) % 2 == 1:
        res[keys_d] = values_d
print(f'{res=}')
print()

#5
print('ex_5')
a = set(dict_a.items())
b = set(dict_b.items())
c = set(dict_c.items())
res = {'dict_a': len(a & c), 'dict_b': len(b & c)}
print(f'{res=}')

