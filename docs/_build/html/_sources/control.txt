Control Flow
============

If statements
-------------

Silicon's if statements check if the top stack item is 1 or not. If it is, it'll run the code.
To create an if statement, enclose the code in parentheses:

::("Hi there")

Comparison operators
--------------------

Comparison operators compare the two top stack items.

* `=` Equal to
* `<` Less than
* `>´ Greater than

Comparison operators can be easily combined with if statements

For loops
---------

Like in Python, Silicon's for loops operate on an iterator.
A for loop's syntax is:

::|code|

The range() builtin
~~~~~~~~~~~~~~~~~~~

To make a list with the numbers in a certain range, use the `\` command as so:

::1_1000_\

The above example pushes a list with the numbers from 1 to 1000.

For (:P) example, here is a snippet that calculates the square roots of all numbers from 1 to 100:

::1_100_\|q|

While loops
-----------

While loops run while the top stack item is 1. To make a while loop, enclose the code in square brackets.

A truth machine using a while loop:

::i[]