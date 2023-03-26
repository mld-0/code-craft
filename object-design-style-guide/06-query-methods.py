#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import unittest
from dataclasses import dataclass
#   Notes:
#   {{{
#   2023-03-26T21:25:16AEDT book uses 'modifier method' to refer specifically to methods to return a modified copy of an immutable class (this is not the wider definition of 'modifier method'?)
#   2023-03-26T22:36:53AEDT how does 6.4 CurrencyConverter go as far as being a well designed set of classes? [...] (the fact 'money.converted(exchangeRate)' requires 'exchangeRate.currency_from' to match the currency of 'money' feels like an indicator this design could be better) [...] (if nothing else, that's a lot of lines to do not much)
#   2023-03-26T22:41:49AEDT 'CounterImmutable' -> (going by the lessons of the book, the ctor should require an argument for 'count', and the creation of a count=0 object should be handled by a factory function) (book is yet to mention default arguments - (java doesn't have them?))
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
@dataclass(frozen=True)
class CounterImmutable:
    count: int = 0
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
#   <>
#   {{{
#class Currency:
#    def __init__(self, code):
#        self.code = code
#    def __eq__(self, lhs):
#        return self.code == lhs.code
#class Money:
#    def __init__(self, amount: int, currency: Currency):
#        self.amount = amount
#        self.currency = Currency
#    def converted(self, exchangeRate: ExchangeRate):
#        if not exchangeRate.currency_from == self.currency:
#            raise Exception("currency of exchangeRate does not match")
#        return Money(self.amount * exchangeRate.rate, exchangeRate.currency_to)
#class ExchangeRate:
#    def __init__(self, currency_from: Currency, currency_to: Currency, rate: float):
#        self.currency_from = currency_from
#        self.currency_to = currency_to
#        self.rate = rate
#class FixerAPI:
#    def exchangeRateFor(currency_from: Currency, currency_to: Currency) -> ExchangeRate:
#        rate = 1.0
#        return ExchangeRate(currency_from, currency_to, rate)
#class CurrencyConverter:
#    def __init__(self, fixerAPI: FixerAPI):
#        self.fixerAPI = fixerAPI
#    def convert(self, money: Money, currency_to: Currency) -> Money:
#        exchangeRate = self.fixerAPI.exchangeRateFor(money.currency, currency_to)
#        return money.converted(exchangeRate)
#   }}}


#   6.5) Define an abstraction for queries that cross system boundaries
#   Any call across a system boundry should be hidden behind an abstraction which:
#           Uses a service interface instead of a service class
#           Leaves out implementation details
#
#   Abstractions make it possible to create test scenarios without making actual network/filesytem calls
#   It also provides us with freedom to change implementation details at a later point
#
#   <>


#   Python and interface classes
#   {{{
#   }}}


#   6.6) Use stubs for test doubles with query methods


#   6.7) Query methods should use other query methods, not command methods


#   Summary:
#   <>

