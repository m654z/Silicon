from functools import *
from commands import *
import time
import cp037
import sys

class Interpreter:
    it = 0
    ifValue = 0
    stack = []
    function = ""
    argFunc = ""
    debug = True
    implicitOutput = True
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

            if code[i] == '=':
                ifValue = int(self.pop() == self.pop())

            elif code[i] == '>':
                ifValue = int(self.pop() > self.pop())

            elif code[i] == '<':
                ifValue = int(self.pop() < self.pop())

            elif code[i] == ',':
                ifValue = 1 - ifValue
                
            elif code[i] in "0123456789":
                self.push(int(code[i]))

            elif code[i] == '¨':
                time.sleep(1)

            elif code[i] == '½':
                self.implicitOutput = False

            elif code[i] == '§':
                self.implicitOutput = True

            elif code[i] == 'V':
                self.stack = self.stack[::-1]

            # Pushes everything in between the quotes on to the stack.
            elif code[i] == '"':
                text = ''
                while i < len(code):
                    i += 1
                    if i == len(code): break
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

            # If statement, runs only if the ifValue is 1
            elif code[i] == '(':
                ifCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == ')': break
                    ifCode += code[i]

                if ifValue == 1:
                    self.run(ifCode)

            # If statement without implicit output.
            elif code[i] == '{':
                ifCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == '}': break
                    ifCode += code[i]

                if ifValue == 1:
                    self.implicitOutput = False
                    self.run(ifCode)
                    self.implicitOutput = True

            # While loop
            elif code[i] == '[':
                loop = ''
                while i < len(code):
                    i += 1
                    if code[i] == ']': break
                    loop += code[i]

                try:
                    while self.peek() != 0:
                        self.run(loop)

                except IndexError:
                     self.push(1)
                     while self.peek() != 0:
                         self.run(loop)

            # Map
            elif code[i] == '\u00AB':
                mapCode = ''
                while i < len(code):
                    i += 1
                    if code[i] == '\u00BB': break
                    mapCode += code[i]

                #mapCode = 'Â' + mapCode
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
                #filterFunc = 'Â' + code[i]
                filterFunc = code[i]
                new = []
                l = self.pop()[::-1]
                for t in l:
                    self.push(l.pop())
                    self.run(filterFunc)
                    if self.pop():
                        self.pop()
                        new.append(self.peekc(2))

                    else:
                        self.pop()

                self.implicitOutput = True
                self.pop()
                self.push(new)
                    
            elif code[i] == '#':
                while i < len(code):
                    i += 1
                    if code[i] == '#': break

            elif code[i] == '|':
                m = False
                forcode = ''
                fin = []
                while i < len(code):
                    i += 1
                    if code[i] == '|': break
                    forcode += code[i]

                if "'" in forcode:
                    m = True
                    after = forcode.split("'")[1]
                    forcode = forcode[0]

                lst = self.pop()
                temp = self.stack
                self.stack = []
                for i in lst:
                    self.push(i)
                    self.run(forcode)

                fin = self.stack

                if m == True:
                    self.run(after)

                self.stack = temp
                self.push(fin)
                
            #elif code[i] == '\u00B2':
            #    i += 1
            #    ALT_COMMANDS.get(self.cp.ord(code[i]), lambda x: x)(self)
                
            else:
                COMMANDS.get(self.cp.ord(code[i]), lambda x: x)(self)
                
            i += 1

        if self.implicitOutput:
            print(self.peek())

i = Interpreter()
#try:
#    if sys.argv[1] == '-i':
#        i.run(sys.argv[2])
#    else:
#        i.run(open(sys.argv[1]).read())

#except:
while 1:
    i.run(input('> '))
