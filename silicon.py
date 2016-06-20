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

            elif code[i] == "`":
                time.sleep(1)

            elif code[i] == '(':
                ifCode = ""
                while i < len(code):
                    i += 1
                    if code[i] == ')':
                        break

                    ifCode += code[i]

                if self.peek() == 1:
                    self.run(ifCode)

            elif code[i] == '[':
                lCode = ""
                while i < len(code):
                    i += 1
                    if code[i] == ']':
                        break

                    lCode += code[i]

                loop = lCode.split('|')
                for i in range(0, int(loop[0])):
                    self.run(loop[1])
                    
            elif code[i] == '"':
                text = ""
                while i < len(code):
                    i += 1
                    if code[i] == '"':
                        break
                    
                    text += code[i]

                self.push(text)

            elif code[i] == "#":
                while i < len(code):
                    i += 1
                    if code[i] == "#":
                        break
                
            else:
                COMMANDS.get(code[i], lambda x:x)(self)
                
            i += 1

i = Interpreter()
