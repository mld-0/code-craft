#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import unittest
#   Notes:
#   {{{
#   2023-03-26T21:25:16AEDT book uses 'modifier method' to refer specifically to methods to return a modified copy of an immutable class (this is not the wider definition of 'modifier method'?)
#   }}}

#   6.1) Use query methods for information retrieval for mutable objects
#   A method should either change something (command method), or return something (query method).
#   A query method returns a value and has no side effects

class CounterMutable:
    def __init__(self):
        self.count = 0
    def currentCount(self) -> int:
        return self.count
    def increment(self):
        self.count += 1

#   For immutable classes, command methods instead return a modified copy of the object
class CounterImmutable:
    def __init__(self):
        self.count = 0
    def incremented(self) -> CounterImmutable:
        return CounterImmutable(self.count + 1)
    def currentCount(self) -> int:
        return self.count


class TestCounter(unittest.TestCase):
    def test_CounterMutable(self):
        c = CounterMutable()
        self.assertEqual(c.currentCount(), 0)
        c.increment()
        self.assertEqual(c.currentCount(), 1)
    def test_CounterImmutable(self):
        c = CounterImmutable()
        c.incremented()
        self.assertEqual(c.currentCount(), 0)
        c = c.incremented()
        self.assertEqual(c.currentCount(), 1)

t = TestCounter()
t.test_CounterMutable()
t.test_CounterImmutable()


#   6.2) Query methods should have a single return type
#   A method that may return one of several types is more difficult to use
# 
#   Some methods may need to indicate failure by returning a null/None value
#   Consider throwing an exception as an alternative to returning null/None
#   Alternatively, use a Result or other type that can represent the null/None case
#   (whichever option is chosen, the client will have to handle the possibility of a null/None case)
#   
#   Use 'getX' to indicate query methods that cannot fail and 'findX' to indicate those that may


#   6.3) Avoid query methods that expose internal state
#   A getter method provides access to an object variable (property)
#   An object should expose no more of its internals than it has to
#
#   Query methods should not use names which might be interpreted as a command
#   contention: use 'itemCount()' instead of 'getItemCount()' or 'countItems()' (since the latter two sound like commands)
#
#   If a particular function requires access to a particular variable of a class, considering making that function part of the class instead of exposing the variable


#   6.4) Define specific methods and types for the queries you want to make

