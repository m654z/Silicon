Basics
======

The stack
---------

Silicon is a stack-based language, meaning that it operates on a single stack. Items can be pushed and popped from the stack.

Pushing strings
~~~~~~~~~~~~~~~

To push a string, enclose it in quotes and it will be automatically pushed on to the stack.

`"Hello, World!"`

Pushing integers
~~~~~~~~~~~~~~~~

To push a single-digit integer, just type the number.

`4`

To push a multi-digit integer, enclose it in underscores.

`_23_`

Popping items
~~~~~~~~~~~~~

To pop the topmost stack item, removing it, use the command `p`.

`"Hello!"p`

Duplicating items
~~~~~~~~~~~~~~~~~

To duplicate the top stack item, use the command `U`.

`"This will be duplicated"U`

Input and output
----------------

To get input, use the `i` command:

`"Hello, what is your name?"i`

To get input and convert it to an integer, you can use the command `I`:

`"What is 2+2?"I`

Output in Silicon is implicit, meaning the top stack item will be displayed once the program has finished running. (There is also a manual output command, `o`)

Here is a very simple cat program:

`i`

If needed, implicit output can be toggled on and off with the commands `½` and `§`, respectively.

Arithmetic
----------

Silicon uses prefix notations, as the integers have to be pushed onto the stack before using an operator.

`_38_4+`

`_44_2-`

`69*`

`_84_2/`