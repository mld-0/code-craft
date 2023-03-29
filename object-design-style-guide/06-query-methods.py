#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import math
import unittest
from dataclasses import dataclass
from abc import ABC, abstractmethod
#   Notes:
#   {{{
#   2023-03-26T21:25:16AEDT book uses 'modifier method' to refer specifically to methods to return a modified copy of an immutable class (this is not the wider definition of 'modifier method'?)
#   2023-03-26T22:36:53AEDT how does 6.4 CurrencyConverter go as far as being a well designed set of classes? [...] (the fact 'money.converted(exchangeRate)' requires 'exchangeRate.currency_from' to match the currency of 'money' feels like an indicator this design could be better) [...] (if nothing else, that's a lot of lines to do not much)
#   2023-03-26T22:41:49AEDT 'CounterImmutable' -> (going by the lessons of the book, the ctor should require an argument for 'count', and the creation of a count=0 object should be handled by a factory function) (book is yet to mention default arguments - (java doesn't have them?))
#   2023-03-28T21:56:10AEDT mock test objects is really a topic for a whole item
#   2023-03-28T22:22:13AEDT 'InvoicePersistance' is a terrible name for a class for saving Invoices to a file(?)
#   2023-03-28T22:26:29AEDT abstract vs interface class?
#   2023-03-29T19:20:55AEDT SOLID-principles: InvoicePersistance and ParkingLot are poor examples(?) [...] (explanations for first link are generally not-the-best)
#   2023-03-29T19:49:50AEDT python's 'ABC' doesn't require derived classes to implement a method unless it is decorated with '@abstractmethod'
#   2023-03-29T20:25:58AEDT purpouse of 'GeneralShapeInterface' class (in addition to 2d/3d-ShapeInterface classes) (second link in SOLID principles section, called 'ManageShapeInterface' in example)  - (used to provide a common interface to different kinds of shapes?)
#   2023-03-29T20:36:38AEDT Dependency inversion principle -> requiring DBConnectionInterface and SQLConnection is unnecessary, since presumably SQLConnection will already be wrapping the actual SQL API (also implementation classes are unlikely to follow or be derived from whatever interface class we define)
#   2023-03-29T20:52:50AEDT "pick a GUID (sufficiently long random number)" seems like a worse solution than just violating command-query separation
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
#   Use names like 'getX' to indicate query methods that cannot fail and 'findX' to indicate those that may


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


#   SOLID principles:
#   {{{
#   LINK: https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/
#   LINK: https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design

#   An abstract class allows derived classes to override methods, an interface class does not allow methods to be implemented


#   Single responsibility principle
#   A class should do one thing, and therefore it should have only a single reason to change
#   (There should only be one aspect of the software's specification which, if changed, would require a class to be changed)
#   Avoid mixing business/persistence logic
#
#   An 'Invoice' class should not be responsible for saving an invoice to a file - define an 'InvoiceSaver' class to handle this


#   Open-closed principle
#   Classes should be open for extension and closed to modification
#   (We should be able to add new functionality without altering the existing class) (and should seek to avoid modifying existing classes)
#   
#   Use Interface classes
#   <(Define an 'InvoiceSaver' abstract class, and create separate 'InvoiceFileSaver' and 'InvoiceDatabaseSaver' to handle saving to files/databases respectively)>
#
#   An 'AreaCalculator' class would need to be modified every time a new shape is added -> suggesting it is the shape classes that should provide an 'area()' method to perform the calculation.
#   (The way to create such an 'AreaCalculator' class would be to define a 'ShapeInterface' class, which can receive any object derived from such an interface an call its get-area method)

class AreaCalculator:
    @staticmethod
    def area(shape: ShapeInterface) -> float:
        return shape.area()
class ShapeInterface(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
class Square(ShapeInterface):
    def __init__(self, length: float):
        self.length = length
    def area(self) -> float:
        return self.length * self.length

x = Square(4)
assert AreaCalculator.area(x) == 16


#   Liskov substitution principle
#   Derived classes should be substitutable for their base class (a subclass is-a base class)
#   <>


#   Interface segregation principle
#   Many client-specific (specialised) interfaces are better than one general-purpose interface
#   Clients wishing to create base classes should not be forced to implement methods they do not need
#   <(don't define a ParkingLot class that handles payment logic and attempt to derive a FreeParkingLot from it, create a single parent class without payment logic and derive separate classes from it for paid/unpaid parking lots)>

class TwoDimensionalShapeInterface(ABC):
    @abstractmethod
    def area(self): raise NotImplementedError()
class ThreeDimensionalShapeInterface(ABC):
    @abstractmethod
    def volume(self): raise NotImplementedError()
class Cube(TwoDimensionalShapeInterface, ThreeDimensionalShapeInterface):
    def __init__(self, length):
        self.length = length
    def area(self):
        return 6 * math.pow(self.length, 2)
    def volume(self):
        return math.pow(self.length, 3)

x = Cube(4)
assert x.area() == 96
assert x.volume() == 64

#   <(optionally, create a 'GeneralShapeInterface', which provides methods/an-interface common to different types of shapes?)>


#   Dependency inversion principle
#   (mechanism for implementing the open-closed principle)
#   High-level classes should depend on interface/abstract classes instead of concrete classes
#   (recall that changing the concrete class implementation should not be a reason for the high-level class to have to change)

class DBConnectionInterface(ABC):
    @abstractmethod
    def connect(self): raise NotImplementedError()
class SQLConnection(DBConnectionInterface):
    def connect(self):
        ...
class PasswordReminder:
    def __init__(self, db: DBConnectionInterface):
        self.db = db

#   }}}


#   Python and interface classes:
#   {{{
#   LINK: https://stackoverflow.com/questions/2124190/how-do-i-implement-interfaces-in-python

#   Using 'abc.ABC':
class Interface(ABC):
    @abstractmethod
    def hello(self):
        return "Default-Hello"
class ImplementationNew(Interface):
    def hello(self):
        return "Hello"

#   Access interface class (default) implementation through 'super()':
class ImplementationDefault(Interface):
    def hello(self):
        return super().hello()

x = ImplementationNew()
assert x.hello() == "Hello"
x = ImplementationDefault()
assert x.hello() == "Default-Hello"

#   Attempting to create an instance of an interface class will fail, as will attempting to create an instance of a subclass that doesn't implement all abstractmethods

#   }}}


#   6.6) Use stubs (mock objects) for test doubles with query methods
#   A stub is a mock test object which returns hardcoded values
#   Separate testing of logic which uses external values from the fetching of those values
#   (A test which relies on the outside world is an integration test, not a unit test)
#   contention: don't use mocking tools for creating stubs, manually created objects will be easier to use and maintain

#   Test method names should be descriptive names, they do not have to be short like method names, they may be whole sentences which describe what is being tested


#   6.7) Query methods should use other query methods, not command methods
#   Query methods should not have side effects, while command methods may
#   Consider separating any query method with side effects into two methods

#   Alternatives/exceptions to command-query separation
#   {{{
#   LINK: https://dzone.com/articles/cqrs-is-an-anti-pattern-for-ddd
#   LINK: https://blog.ploeh.dk/2014/08/11/cqs-versus-server-generated-ids/

#   Command-query separation is helpful where scalability is required, but can otherwise unnecessarily complicate designs

#   Obvious exception: stack.pop()

#   Using a GUID is an alternative to a 'saveToDatabase()' needing to return an id for the new record
#   (a randomly generated number long enough to be almost certain to be unique, provided by the caller)

#   }}}


#   Summary:
#   A query method retrieves a piece of information. They should have a single return type (and consider alternatives to returning null/None). 
#   Query methods should not have side effects, and should expose as little of an objects internals as possible.
#   Define specific query methods for each question you want to ask.
#   Define an abstraction wherever queries cross system boundaries
#   Use mock objects when testing code that relies on queries that cross system boundaries.

