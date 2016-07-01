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
    implicitOutput = True
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

            # For loop. Warning: buggy
            # Syntax: òcodeò
            elif code[i] == 'ò':
                forCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == 'ò': break
                    forCode += code[i]

                for i in self.peek():
                    self.run(forCode)

            elif code[i] == 'Â':
                self.implicitOutput = False

            elif code[i] == '§':
                self.implicitOutput = True

            # Runs a function with arguments. (Argumental function? :P)
            # Syntax: &arg1|arg2&
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

            # Defines a function with arguments.
            # @ will be replaced with arg1 and ? with arg2.
            # Syntax: ´code´.
            elif code[i] == "´":
                func = ''
                while i < len(code):
                    i += 1
                    if code[i] == "´": break
                    func += code[i]

                self.argFunc = func
                if self.debug == True:
                    print("ArgFunc: " + self.argFunc)


            # Commands for working with the ASCII art module
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

            # Pushes everything in between the quotes on to the stack.
            elif code[i] == '"':
                text = ''
                while i < len(code):
                    i += 1
                    if code[i] == '"': break
                    text += code[i]

                self.push(text)

            # Replacement.
            # Syntax: `replaceThis|withThis`
            elif code[i] == '`':
                replace = ''
                while i < len(code):
                    i += 1
                    if code[i] == '`': break
                    replace += code[i]

                r = replace.split('|')
                self.push(self.pop().replace(r[0], r[1]))

            # Pushes a multi-digit number on to the stack.
            elif code[i] == '_':
                num = ''
                while i < len(code):
                    i += 1
                    if code[i] == '_': break
                    num += code[i]

                self.push(int(num))

            # Anonymous function.
            # Syntax: {code}
            elif code[i] == '{':
                func = ''
                while i < len(code):
                    i += 1
                    if code[i] == '}': break
                    func += code[i]

                self.function = func

            # If statement, runs only if the top stack value is 1
            elif code[i] == '(':
                ifCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == ')': break
                    ifCode += code[i]

                if self.peek() == 1:
                    self.run(ifCode)

            # While loop
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

            # If statement.
            # Syntax: :ifThis|code:
            elif code[i] == ':':
                ifCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == ':': break
                    ifCode += code[i]

                ic = ifCode.split('|')
                try:
                    if self.peek() == int(ic[0]):
                        self.run(ic[1])

                except:
                    if self.peek() == ic[0]:
                        self.run(ic[1])

            # Map
            elif code[i] == '\u00AB':
                mapCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == '\u00BB': break
                    mapCode += code[i]

                mapCode = 'Â' + mapCode
                new = []
                for t in self.peek():
                    self.push(t)
                    self.run(mapCode)
                    new.append(self.pop())

                self.implicitOutput = True
                self.pop()
                self.push(new)

            # Filter
            elif code[i] == '\u00A6':
                i += 1
                filterFunc = 'Â' + code[i]
                new = []
                for t in self.peek():
                    self.push(t)
                    self.run(filterFunc)
                    if self.pop():
                        new.append(self.pop())

                    else:
                        self.pop()

                self.implicitOutput = True
                self.pop()
                self.push(new)
                    
            elif code[i] == '#':
                while i < len(code):
                    i += 1
                    if code[i] == '#': break

            elif code[i] == '\u00B2':
                i += 1
                ALT_COMMANDS.get(self.cp.ord(code[i]), lambda x: x)(self)
                
            else:
                COMMANDS.get(self.cp.ord(code[i]), lambda x: x)(self)
                
            i += 1

        if self.implicitOutput:
            print(self.peek())

i = Interpreter()
try:
    if sys.argv[1] == '-i':
        i.run(sys.argv[2])
    else:
        i.run(open(sys.argv[1]).read())

except:
    pass
