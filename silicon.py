from functools import *
from commands import *
import time
import ascii_lib
import cp037
import sys

class Interpreter:
    grid = 0
    it = 0
    stack = []
    function = ""
    argFunc = ""
    debug = False
    asc = ascii_lib.AsciiArt()
    cp = cp037.CP037()

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def peekc(self, i):
        return self.stack[-i]

    def clr(self):
        s = self.stack
        self.stack = []
        return s

    def get(self):
        a = self.pop()
        b = self.peek()
        self.push(a)
        return b

    def run_func(self):
        self.run(self.function)

    def run(self, code):
        i = 0
        while i < len(code):
            if self.debug == True:
                print(self.stack)
                print(code[i])
                
            if code[i] in "0123456789":
                self.push(int(code[i]))

            elif code[i] == '¨':
                time.sleep(1)

            elif code[i] == ',':
                pass

            elif code[i] == '&':
                arg = ''
                arg2 = ''
                while i < len(code): 
                    i += 1
                    if code[i] == '&': break
                    arg += code[i]

                if '|' in arg:
                    arg = arg.split('|')
                    arg2 = arg[1]
                    arg = arg[0]

                self.run(self.argFunc.replace('@', arg).replace('?', arg2))

            elif code[i] == 'V':
                self.stack = self.stack[::-1]

            elif code[i] == "´":
                func = ''
                while i < len(code):
                    i += 1
                    if code[i] == "´": break
                    func += code[i]

                self.argFunc = func
                if self.debug == True:
                    print("ArgFunc: " + self.argFunc)

            elif code[i] == 'Ù':
                forCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == ';': break
                    forCode += code[i]

                s = list(self.peek())
                for l in s:
                    self.push(l)
                    self.run(forCode)
                    self.pop()

            elif code[i] == 'Å':
                while i < len(code):
                    i += 1
                    if code[i] == 'Å': break

                    if code[i] == 's':
                        self.push(self.asc.grid)

                    elif code[i] == 'p':
                        pprint.pprint(self.asc.grid)

                    elif code[i] == 'd':
                        self.asc.draw(self.pop(), self.pop(), self.pop())

                    elif code[i] == 'm':
                        self.asc.move(self.pop(), self.pop(), self.pop(),
                                      self.pop())

                    elif code[i] == 'e':
                        self.asc.erase(self.pop(), self.pop())

                    elif code[i] == 'G':
                        self.asc.draw_ground()

                    elif code[i] == 'C':
                        self.asc.draw_ceil()

            elif code[i] == '"':
                text = ''
                while i < len(code):
                    i += 1
                    if code[i] == '"': break
                    text += code[i]

                self.push(text)

            elif code[i] == '`':
                replace = ''
                while i < len(code):
                    i += 1
                    if code[i] == '`': break
                    replace += code[i]

                r = replace.split('|')
                self.push(self.pop().replace(r[0], r[1]))


            elif code[i] == '_':
                num = ''
                while i < len(code):
                    i += 1
                    if code[i] == '_': break
                    num += code[i]

                self.push(int(num))

            elif code[i] == '{':
                func = ''
                while i < len(code):
                    i += 1
                    if code[i] == '}': break
                    func += code[i]

                self.function = func

            elif code[i] == '(':
                ifCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == ')': break
                    ifCode += code[i]

                if self.peek() == 1:
                    self.run(ifCode)

            elif code[i] == '[':
                loop = ''
                while i < len(code):
                    i += 1
                    if code[i] == ']': break
                    loop += code[i]

                if '|' in loop:
                    loop = loop.split('|')
                    self.run(loop[0])
                    while self.peek() != 0:
                        self.run(loop[1])

                else:
                    while self.peek() != 0:
                        self.run(loop)

                self.it = 0

            elif code[i] == ':':
                ifCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == ':': break
                    ifCode += code[i]

                i = ifCode.split('|')
                if self.peek() == i[0]:
                    self.run(i[1])
                    
            elif code[i] == '#':
                while i < len(code):
                    i += 1
                    if code[i] == '#': break
                
            else:
                COMMANDS.get(self.cp.ord(code[i]), lambda x: x)(self)
                
            i += 1

        print(self.peek())

i = Interpreter()
if sys.argv[1] == '-i':
    i.run(sys.argv[2])
else:
    i.run(open(sys.argv[1]).read())
