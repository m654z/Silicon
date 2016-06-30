2. Simple programs
==================

Let's learn a bit about Silicon by writing some simple programs.

2.1 Hello, world!
-----------------

As you might know, the first program you usually write when learning a new programming language is a program that outputs "Hello, world!"
Let's try that out in Silicon!

``"Hello, world!"``

Silicon is a stack-based language, meaning that it operates on a single stack. Everything between the quotes (`" "`) are pushed on top of the stack. Output is implicit in Silicon (the top stack item will be outputted), so there is no need for an output command in the above example.

2.2 Math
--------

Silicon uses postfix notation (expressions like `55+`), so normal expressions like `5+5` are not valid. This is because numbers in code are pushed on the stack, and arithmetical commands operate on the 2nd-top and 3rd-top items.
Silicon supports the four main arithmetical operators: addition, subtraction, multiplication, and division, as well as modulo and exponent.

2.3 Input and output
--------------------

To get input, there are two commands you can use: `i` and `I`.
`i` gets input as a string and pushes it on the stack. `I` gets input as an integer and pushes it on the stack.
`o` outputs the top stack item, but this is usually unneeded, as output in Silicon is implicit.

A simple cat program (a program that copies its input to its output) is only one byte long: `i`.

2.4 Conditional statements
--------------------------

There are a few conditional operators, which return 1 if the contition is True, and 0 if it's False.
`<` checks if an integer is greater than another one. `>` checks if an integer is less than another. `=` checks if two integers are equal.
Of course, you can't do anything useful with those values without conditional statements. In Silicon, everything between parentheses `()` are run only if the top stack value is 1. If it isn't, the code is skipped altogether.
So, for example the program `ÂII=("Equal!"o)` would check if two number are equal, and output "Equal!" if it's true. Note the `Â`: it toggles implicit output. If implicit output would be toggled on, and the above program would be run, it would output "Equal!" no matter what.

2.5 Loops
---------

Silicon only has one kind of loop: the while loop. Everything between square brackets `[]` are run while the top stack value is 1.
For loops, however, can be simulated using while loops, using the syntax `[times|Dcode]`. Everything before the `|` is run once before the actual loop code, so for example `[5|D]` would count down from 5. `D` decrements the top stack value.

2.6 Functions
-------------

There are two kinds of functions: code blocks, and functions with arguments. You can set the value of the code block by putting some code in between the curly braces `{}`. The code block can then be run by using the command `C`.
Functions with arguments are a bit different. They can be used in the same way as code blocks, but you can also pass arguments to them. For example, the code `´"@"o´` takes one argument, and outputs it. They support up to two arguments, and can be run with the syntax `&arg1|arg2&`.