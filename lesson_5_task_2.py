"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


map = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    '10': 'a',
    '11': 'b',
    '12': 'c',
    '13': 'd',
    '14': 'e',
    '15': 'f',

}

one = list(input('Введите число в шестнадцатеричной системе '
                          'счисления: '))
tow = list(input('Введите число в шестнадцатеричной системе '
                          'счисления: '))
def sum16(one, tow):
    u = 0
    val = deque()
    for i in range(1, max(len(one), len(tow)) + 1):
        try:
            a = int(one[-i])
        except ValueError:
            a = map[str(one[-i])]
        except IndexError:
            a = 0
        try:
            b = int(tow[-i])
        except ValueError:
            b = map[str(tow[-i])]
        except IndexError:
            b = 0
        c = a + b + u
        if c >= 16:
            z = c - 16
            u = 1
        else:
            z = c
            u = 0
        val.appendleft(str(map[str(z)]))
    if u:
        val.appendleft(str(map[str(u)]))
    return map["".join(val)] if len(val) == 1 else "".join(val)

def mul16(one, tow):
    end = deque()
    a, b = (one, tow) if len(one) >= len(tow) else (tow, one)
    for k, i in enumerate(reversed(a), 0):
        val = deque()
        u = 0
        for f in reversed(b):
            c = map[i] * map[f] + u
            if c >= 16:
                h = c // 16
                z = c - h * 16
                val.appendleft(map[str(z)])
                u = h
            else:
                u = 0
                val.appendleft(map[str(c)])
        if u:
            val.appendleft(map[str(u)])
        val.extend(['0'] * k)
        end.append(val)
    q = None
    for i in range(len(end)):
        if not q:
            q = end[i]
        else:
            q = sum16(q, end[i])
    return q

print(sum16(one, tow))
print(mul16(one, tow))
