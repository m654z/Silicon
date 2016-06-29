from functools import *
from itertools import count, islice
from math import sqrt
import random
import math
import base64
import itertools
import operator
import statistics
try:
    from fractions import gcd
except ImportError:
    from math import gcd

def add(val1, val2):
    return val1 + val2

def sub(val1, val2):
    return val1 - val2

def mul(val1, val2):
    return val1 * val2

def div(val1, val2):
    return val1 / val2

def mod(val1, val2):
    return val1 % val2

def exp(val1, val2):
    return val1 ** val2

def shift(n, t):
    k = "abcdefghijklmnopqrstuvwxyz"
    r = ''
    for l in t.lower():
        try:
            i = (k.index(l) + n) % 26
            r += k[i]

        except ValueError:
            r += 1

    return r.lower()

def var_type(var):
    if type(var) is int:
        return "int"

    elif type(var) is str:
        return "str"

    elif type(var) is float:
        return "float"

    elif type(var) is list:
        return "list"

    else:
        return "other"

def fibonacci(n):
    p,c,r = 0,0,0
    for i in range(0, n):
        r = p + c
        p = c
        c = r

    return r

def is_prime(n):
    p = n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    if p == True:
        return 1
    else:
        return 0

def is_greater(n1, n2):
    if n1 > n2:
        return 1

    else:
        return 0

def is_less(n1, n2):
    if n1 < n2:
        return 1

    else:
        return 0

def is_equal(n1, n2):
    if n1 == n2:
        return 1

    else:
        return 0

def list_sum(l):
    n = 0
    for i in l:
        n += int(i)

    return n

def int_list(l):
    return list(map(int, l))

def read_file(f):
    f = open(f, 'r')
    text = f.read()
    f.close()
    return text

def write_file(t, f):
    f = open(f, 'rw')
    f.write(t)
    f.close()

def hello(n):
    if n == 0: return "Hello World!"
    elif n == 1: return "Hello, World!"
    elif n == 2: return "Hello world!"
    elif n == 3: return "Hello, world!"

COMMANDS = {
    78: lambda x:x.push(add(x.pop(), x.pop())),
    96: lambda x:x.push(sub(x.pop(), x.pop())),
    92: lambda x:x.push(mul(x.pop(), x.pop())),
    97: lambda x:x.push(div(x.pop(), x.pop())),
    176: lambda x:x.push(exp(x.pop(), x.pop())),
    90: lambda x:x.push(math.factorial(x.pop())),
    110: lambda x:x.push(is_greater(x.pop(), x.pop())),
    76: lambda x:x.push(is_less(x.pop(), x.pop())),
    126: lambda x:x.push(is_equal(x.pop(), x.pop())),
    129: lambda x:x.push("abcdefghijklmnopqrstuvwxyz"),
    130: lambda x:x.push(math.ceil(x.pop())),
    131: lambda x:x.push("123567890"),
    132: lambda x:x.push(eval(x.pop())),
    133: lambda x:x.push(math.floor(x.pop())),
    134: lambda x:x.push(chr(x.peek())),
    137: lambda x:x.push(input()),
    145: lambda x:x.push(''.join(x.pop())),
    146: lambda x:x.push(x.pop()[int(x.pop())]),
    147: lambda x:x.push(x.pop().lower()),
    148: lambda x:x.push(mod(x.pop(), x.pop())),
    149: lambda x:x.push(int(x.pop())),
    150: lambda x:print(x.peek()),
    151: lambda x:x.pop(),
    152: lambda x:x.push(math.sqrt(x.pop())),
    153: lambda x:x.push(random.randint(0, 100)),
    162: lambda x:x.push(x.peek()*x.pop()),
    163: lambda x:x.push(var_type(x.peek())),
    164: lambda x:x.push(x.pop().upper()),
    166: lambda x:x.push(read_file(x.pop())),
    167: lambda x:x.push(x.pop().extend(x.pop())),
    168: lambda x:x.push(len(x.peek())),
    169: lambda x:x.push(shift(x.pop(), x.pop())),
    193: lambda x:x.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    194: lambda x:x.push(base64.b64encode(x.pop())),
    195: lambda x:x.run_func(),
    196: lambda x:x.push(int(x.pop())-1),
    197: lambda x:x.push(x.run(x.pop())),
    198: lambda x:x.push(fibonacci(x.peek())),
    199: lambda x:x.push(x.peek().pop()),
    200: lambda x:x.push(int(x.pop())/2),
    201: lambda x:x.push(int(input())),
    209: lambda x:x.push(x.pop().append(x.pop())),
    210: lambda x:x.push(gcd(x.pop(), x.pop())),
    211: lambda x:x.push(x.peek().length()),
    212: lambda x:x.push(list_sum(x.pop())),
    213: lambda x:x.push(int(x.pop())+1),
    214: lambda x:x.push(ord(x.peek())),
    215: lambda x:x.push(is_prime(x.pop())),
    216: lambda x:x.push(sorted(x.pop())),
    217: lambda x:x.push(x.pop()[::-1]),
    226: lambda x:x.push(list(str(x.pop()))),
    227: lambda x:x.push(int_list(x.pop())),
    228: lambda x:x.push(x.peek()),
    230: lambda x:write_file(x.pop(), x.pop()),
    231: lambda x:random.shuffle(x.peek()),
    232: lambda x:x.push(x.pop().split(x.pop())),
    233: lambda x:x.push(len(x.peek().encode('utf-8'))),
    101: lambda x:x.push(str(x.pop()).replace(str(x.pop()), '')),
    113: lambda x:x.push(statistics.mean(x.peek())),
    117: lambda x:x.push(statistics.mode(x.peek())),
    238: lambda x:x.push(statistics.median(x.peek())),
    100: lambda x:x.push(str(x.pop()) + str(x.pop())),
    116: lambda x:x.push(x.pop().split(',')),
    120: lambda x:x.push(str(x.pop())*x.pop()),
    237: lambda x:x.push(reduce(operator.mul, x.pop(), 1)),
    253: lambda x:x.push([]),
    98: lambda x:x.push(10),
    114: lambda x:x.peek().extend(x.pop()),
    118: lambda x:x.peek().insert(x.peekc(2), x.pop()),
    235: lambda x:x.push(100),
    251: lambda x:x.push(255),
    99: lambda x:x.push(x.peekc(2)),
    115: lambda x:x.push(x.peek() ^ x.peekc(2)),
    119: lambda x:x.push(x.peek() << x.peekc(2)),
    236: lambda x:x.push(x.peekc(3)),
    252: lambda x:x.push(x.peek() >> x.peekc(2)),
    102: lambda x:x.push(x.peek() & x.peekc(2)),
    105: lambda x:x.push(~x.peek()),
    239: lambda x:x.push(x.peek() | x.peekc(2)),
    224: lambda x:x.push(list(range(x.peekc(2), x.peek()+1))),
}
