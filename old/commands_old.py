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
    '+': lambda x:x.push(add(x.pop(), x.pop())),
    '-': lambda x:x.push(sub(x.pop(), x.pop())),
    '*': lambda x:x.push(mul(x.pop(), x.pop())),
    '/': lambda x:x.push(div(x.pop(), x.pop())),
    '^': lambda x:x.push(exp(x.pop(), x.pop())),
    '!': lambda x:x.push(math.factorial(x.pop())),
    '>': lambda x:x.push(is_greater(x.pop(), x.pop())),
    '<': lambda x:x.push(is_less(x.pop(), x.pop())),
    '=': lambda x:x.push(is_equal(x.pop(), x.pop())),
    'a': lambda x:x.push("abcdefghijklmnopqrstuvwxyz"),
    'b': lambda x:x.push(" "),
    'c': lambda x:x.push(math.ceil(x.pop())),
    'd': lambda x:x.push("123567890"),
    'e': lambda x:x.push(eval(x.pop())),
    'f': lambda x:x.push(math.floor(x.pop())),
    'h': lambda x:x.push(chr(x.peek())),
    'i': lambda x:x.push(input()),
    'j': lambda x:x.push(''.join(x.pop())),
    'k': lambda x:x.push(x.pop()[int(x.pop())]),
    'l': lambda x:x.push(x.pop().lower()),
    'm': lambda x:x.push(mod(x.pop(), x.pop())),
    'n': lambda x:x.push(int(x.pop())),
    'o': lambda x:print(x.peek()),
    'p': lambda x:x.pop(),
    'q': lambda x:x.push(math.sqrt(x.pop())),
    'r': lambda x:x.push(random.randint(0, 100)),
    's': lambda x:x.push(x.peek()*x.pop()),
    't': lambda x:x.push(var_type(x.peek())),
    'u': lambda x:x.push(x.pop().upper()),
    'w': lambda x:x.push(read_file(x.pop())),
    'x': lambda x:x.push(x.pop().extend(x.pop())),
    'y': lambda x:x.push(len(x.peek())),
    'z': lambda x:x.push(shift(x.pop(), x.pop())),
    'A': lambda x:x.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    'B': lambda x:x.push(base64.b64encode(x.pop())),
    'C': lambda x:x.run_func(),
    'D': lambda x:x.push(int(x.pop())-1),
    'E': lambda x:x.push(x.run(x.pop())),
    'F': lambda x:x.push(fibonacci(x.peek())),
    'G': lambda x:x.push(x.peek().pop()),
    'H': lambda x:x.push(int(x.pop())/2),
    'I': lambda x:x.push(int(input())),
    'J': lambda x:x.push(x.pop().append(x.pop())),
    'K': lambda x:x.push(gcd(x.pop(), x.pop())),
    'M': lambda x:x.push(list_sum(x.pop())),
    'N': lambda x:x.push(int(x.pop())+1),
    'O': lambda x:x.push(ord(x.peek())),
    'P': lambda x:x.push(is_prime(x.pop())),
    'Q': lambda x:x.push(sorted(x.pop())),
    'R': lambda x:x.push(x.pop()[::-1]),
    'S': lambda x:x.push(list(str(x.pop()))),
    'T': lambda x:x.push(int_list(x.pop())),
    'U': lambda x:x.push(x.peek()),
    'W': lambda x:write_file(x.pop(), x.pop()),
    'X': lambda x:random.shuffle(x.peek()),
    'Y': lambda x:x.push(x.pop().split(x.pop())),
    'Z': lambda x:x.push(len(x.peek().encode('utf-8'))),
    'Á': lambda x:x.push(str(x.pop()).replace(str(x.pop()), '')),
    'É': lambda x:x.push(statistics.mean(x.peek())),
    'Í': lambda x:x.push(statistics.mode(x.peek())),
    'Ó': lambda x:x.push(statistics.median(x.peek())),
    'À': lambda x:x.push(str(x.pop()) + str(x.pop())),
    'È': lambda x:x.push(x.pop().split(',')),
    'Ì': lambda x:x.push(str(x.pop())*x.pop()),
    'Ò': lambda x:x.push(reduce(operator.mul, x.pop(), 1)),
    'Ù': lambda x:x.push([]),
    'Â': lambda x:x.push(10),
    'Ê': lambda x:x.peek().extend(x.pop()),
    'Î': lambda x:x.peek().insert(x.peekc(2), x.pop()),
    'Ô': lambda x:x.push(100),
    'Û': lambda x:x.push(255),
    'Ä': lambda x:x.push(x.peekc(2)),
    'Ë': lambda x:x.push(x.peek() ^ x.peekc(2)),
    'Ï': lambda x:x.push(x.peek() << x.peekc(2)),
    'Ö': lambda x:x.push(x.peekc(3)),
    'Ü': lambda x:x.push(x.peek() >> x.peekc(2)),
    'Ã': lambda x:x.push(x.peek() & x.peekc(2)),
    'Ñ': lambda x:x.push(~x.peek()),
    'Õ': lambda x:x.push(x.peek() | x.peekc(2)),
    '\\': lambda x:x.push(list(range(x.peekc(2), x.peek()+1))),
    '¤': lambda x:x.push(hello(x.pop())),
}
