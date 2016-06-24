from functools import *
from commands import *
import time

class Interpreter:
    stack = []
    function = ""
    debug = False

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

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

            elif code[i] == '`':
                time.sleep(1)

            elif code[i] == ',':
                pass

            elif code[i] == 'V':
                self.stack = self.stack[::-1]

            elif code[i] == '"':
                text = ''
                while i < len(code):
                    i += 1
                    if code[i] == '"': break
                    text += code[i]

                self.push(text)

            elif code[i] == '´':
                replace = ''
                while i < len(code):
                    i += 1
                    if code[i] == '´': break
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

                while self.peek() != True:
                    self.run(loop)
                    
            elif code[i] == '#':
                while i < len(code):
                    i += 1
                    if code[i] == '#': break
                
            else:
                COMMANDS.get(code[i], lambda x:x)(self)
                
            i += 1

i = Interpreter()
