Strings
=======

Pushing strings
---------------

To push a string onto the stack, enclose it in quotes.

`"Hello, World!"`

String manipulation
-------------------

* `R` Reverse
* `²s` Swapcase
* `²t` Titlecase
* `²u` Uppercase

* `Á` Remove a substring from a string

* `²x` Split string at substring, push first part
* `²y` Split string at substring, push second part

Replacement
-----------

To replace a substring with another, use the following syntax:

`(backtick)replaceThis|withThis(backtick)`

For example:

`(bt)cat|dog(bt)`

Converting strings to lists
---------------------------

* `S` Split string
* `²n` Split at newlines
* `²p` Split at spaces
* `²Ë` Split into chunks of two

Other
-----

* `L` Get the length of a string
* `Z` Get the length of a UTF-8 encoded string
* `Ì` Concatenate a string with itself _n_ times
* `n` Convert a string to an integer