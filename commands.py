from functools import *
from itertools import *
from math import sqrt
import random
import math
import base64
import itertools
import operator
import statistics
import urllib.request
import string
import re
import sys
try:
    from fractions import gcd
except ImportError:
    from math import gcd
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup not installed.")

del1 = ''.join(c for c in map(chr, range(256)) if not c in string.ascii_letters)
del2 = ''.join(c for c in map(chr, range(256)) if not c.isdigit())

def not_implemented_error():
    return "Command not implemented yet."

def add(val1, val2):
    if type(val2) is list:
        val2.append(val1)

    elif type(val1) is list and type(val2) is list:
        val2.extend(val1)

    else:
        return val2 + val1

def sub(val1, val2):
    if type(val1) is str and type(val2) is list:
        val2.remove(val1)

    elif type(val1) is int and type(val2) is str:
        return val2[val1:]

    elif type(val1) is int and type(val2) is list:
        return val2[val1]

    else:
        return val1 - val2

def mul(val1, val2):
    if type(val1) is int and type(val2) is str:
        return val2 * val1

    elif type(val2) is list:
        return val2.append(val1)

    else:
        return val1 * val2

def div(val1, val2):
    if type(val1) is int and type(val2) is str:
        return val2[:val1]

    else:
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
    if type(n1) == list:
        if n1[0] > n1[1]:
            return 1

        else:
            return 0
        
    if n1 > n2:
        return 1

    else:
        return 0

def is_less(n1, n2):
    if type(n1) == list:
        if n1[0] < n1[1]:
            return 1

        else:
            return 0
        
    if n1 < n2:
        return 1

    else:
        return 0

def is_equal(n1, n2):
    if type(n1) == list:
        if n1[0] == n1[1]:
            return 1

        else:
            return 0
        
    if n1 == n2:
        return 1

    else:
        return 0

def contains(s1, s2):
    if s1 in s2:
        return 1
    else:
        return 0

def in_list(l, c):
    if c in l:
        return 1
    
    else:
        return 0

def list_sum(l):
    n = 0
    for i in l:
        n += int(i)

    return n

def join(c, l):
    l = c.join(l)
    #l = l[1:]
    return l

def int_list(l):
    return list(map(int, l))

def split_list(s, l):
    new = []
    i = l.index(s)
    while i < len(l):
        new.append(l[i])
        i += 1

    return new

def split_list2(s, l):
    i = l.index(s)
    return l[:i]

# From a SO answer. Thanks sweeneyrod!
def chunks(l, s):
    return (s[0+i:l+i] for i in range(0, len(s), l))

def read_file(f):
    f = open(f, 'r')
    text = f.read()
    f.close()
    return text

def write_file(t, f):
    f = open(f, 'rw')
    f.write(t)
    f.close()

def get_text(url):
   html = urllib.request.urlopen(url).read()
   soup = BeautifulSoup(html, "html.parser")
   [s.extract() for s in soup(['style', 'script', '[document]',
                               'head', 'title'])]
   text = soup.getText()
   return text

def translate(table, text):
    p = re.compile('|'.join(table.keys()))
    return p.sub(lambda x: table[x.group()], text)

def list_to_str(lst):
    l = [str(n) for n in lst]
    return ''.join(l)
	
def rotate(l, n):
    return l[n:] + l[:n]

COMMANDS = {
    78: lambda x:x.push(add(x.pop(), x.pop())),
    96: lambda x:x.push(sub(x.pop(), x.pop())),
    92: lambda x:x.push(mul(x.pop(), x.pop())),
    97: lambda x:x.push(div(x.pop(), x.pop())),
    95: lambda x:x.push(exp(x.pop(), x.pop())),
    90: lambda x:x.push(math.factorial(x.pop())),
    110: lambda x:x.push(is_greater(x.pop(), x.pop())),
    76: lambda x:x.push(is_less(x.pop(), x.pop())),
    126: lambda x:x.push(is_equal(x.pop(), x.pop())),
    129: lambda x:x.push("abcdefghijklmnopqrstuvwxyz"),
    130: lambda x:x.push(" "),
    131: lambda x:x.push(math.ceil(x.pop())),
    132: lambda x:x.push("123567890"),
    133: lambda x:x.push(eval(x.pop())),
    134: lambda x:x.push(math.floor(x.pop())),
    136: lambda x:x.push(chr(x.peek())),
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
    209: lambda x:x.push(x.pop())().append(x.pop()),
    210: lambda x:x.push(gcd(x.pop(), x.pop())),
    211: lambda x:x.push(len(x.peek())),
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
    68: lambda x:x.push(math.pi),
    84: lambda x:x.push(math.e),
    88: lambda x:x.push((1+5**0.5)/2),
    69: lambda x:x.push(x.pop().count(x.peek())),
    81: lambda x:x.push(abs(x.pop()-x.pop())),
    88: lambda x:x.push(in_list(x.peek(), x.pop())),
    86: lambda x:x.push([v for s in x.pop() for v in s]),
    101: lambda x:x.push(str(x.pop()).replace(str(x.pop()), '')),
    113: lambda x:x.push(statistics.mean(x.peek())),
    117: lambda x:x.push(statistics.mode(x.peek())),
    254: lambda x:x.push(list(enumerate(x.pop()))),
    238: lambda x:x.push(statistics.median(x.peek())),
    116: lambda x:x.push(x.pop().split(',')),
    237: lambda x:x.push(reduce(operator.mul, x.pop(), 1)),
    253: lambda x:x.push([]),
    98: lambda x:x.push(10),
    114: lambda x:x.peek().extend(x.pop()),
    118: lambda x:x.peek().insert(x.peekc(2), x.pop()),
    235: lambda x:x.push(100),
    251: lambda x:x.push(255),
    99: lambda x:print(x.peekc(2)),
    115: lambda x:x.push(x.peek() ^ x.peekc(2)),
    119: lambda x:x.push(x.peek() << x.peekc(2)),
    236: lambda x:print(x.peekc(3)),
    #223: lambda x:x.push(list(c*-~i for i,c in x.pop())),
    252: lambda x:x.push(x.peek() >> x.peekc(2)),
    102: lambda x:x.push(x.peek() & x.peekc(2)),
    105: lambda x:x.push(~x.peek()),
    239: lambda x:x.push(x.peek() | x.peekc(2)),
    224: lambda x:x.push(list(range(x.peekc(2), x.peek()+1))),
    156: lambda x:x.push(' '),
    67: lambda x:print(' '.join(x.stack)),
    66: lambda x:print(''.join(x.stack)),
    70: lambda x:x.push(x.pop()*int(input())),
    71: lambda x:x.push(chunks(x.pop(), x.pop())),
    120: lambda x:x.push(' '.join(x.pop())),
    82: lambda x:x.push('\n'.join(x.pop())),
    203: lambda x:x.push(x.pop().translate(None, del1)),
    204: lambda x:x.push(x.pop().translate(None, del2)),
    73: lambda x:x.push(list_to_str(x.pop())),
    89: lambda x:x.push(contains(x.peek(), x.peekx(2))),
    80: lambda x:x.push(x.pop()[-x.pop():]),
    91: lambda x:x.push(list(product(x.pop(), x.pop()))),
    94: lambda x:x.push(rotate(x.pop(), x.pop())),
    104: lambda x:x.push(float(x.pop())),
    108: lambda x:x.push(join(x.pop(), x.pop())),
    111: lambda x:x.push(x.pop().swapcase()),
    112: lambda x:x.push(''.join(list(x.pop())[1:])),
    122:lambda x:x.push(x.pop().upper()),
    124: lambda x:x.push('\n'),
    125: lambda x:x.push(x.pop().lower()),
    128: lambda x:x.push(x.pop().title()),
    140: not_implemented_error(),
    141: not_implemented_error(),
    142: not_implemented_error(),
    143: not_implemented_error(),
    144: lambda x:x.push(dict(zip(x.pop(), x.pop()))),
    154: lambda x:x.push(x.peek()[0]),
    155: lambda x:x.push(x.peek()[-1]),
    157: not_implemented_error(),
    158: not_implemented_error(),
    159: lambda x:x.push(str(x.pop())),
    160: not_implemented_error(),
    161: lambda x:x.push(random.randint(0, x.peek())),
    172: not_implemented_error(),
    173: not_implemented_error(),
    174: not_implemented_error(),
    175: not_implemented_error(),
    177: not_implemented_error(),
    178: not_implemented_error(),
    179: not_implemented_error(),
    180: not_implemented_error(),
    182: not_implemented_error(),
    183: not_implemented_error(),
    185: not_implemented_error(),
    188: not_implemented_error(),
    190: not_implemented_error(),
    191: not_implemented_error(),
    205: lambda x:x.push(split_list2(x.pop(), x.pop())),
    206: lambda x:x.push(split_list(x.pop(), x.pop())),
    207: lambda x:sys.exit(),
    218: not_implemented_error(),
    219: not_implemented_error(),
    220: lambda x:x.push(min(x.peek())),
    221: lambda x:x.push(max(x.peek())),
    222: not_implemented_error(),
    225: not_implemented_error(),
    250: not_implemented_error(),
	107: lambda x:x.push(1 - x.pop()),
}

ALT_COMMANDS = {
    #115: lambda x:x.push(chunks(x.pop(), 2)),
    #131: lambda x:x.push(list(product(x.pop(), x.pop()))),
    #134: lambda x:x.push(float(x.pop())),
    #137: lambda x:x.push(min(x.peek())),
    #145: lambda x:x.push(join(x.pop(), x.pop())),
    #147: lambda x:x.push(x.pop().lower()),
    #148: lambda x:x.push(max(x.peek())),
    #149: lambda x:x.push(x.pop().split('\n')),
    #151: lambda x:x.push(x.pop().split(' ')),
    #153: lambda x:x.push(rotate(x.pop(), x.pop())),
    #162: lambda x:x.push(x.pop().swapcase()),
    #163: lambda x:x.push(x.pop().title()),
    #164: lambda x:x.push(x.pop().upper()),
    #166: lambda x:x.push(get_text(x.pop())),
    #167: lambda x:x.push(split_list2(x.pop(), x.pop())),
    #169: lambda x:x.push(split_list(x.pop(), x.pop())),
}
