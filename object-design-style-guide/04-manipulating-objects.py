#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import unittest
#   Ongoings:
#   {{{ 
#   Ongoing: 2023-03-24T22:29:59AEDT does 'entity' imply "has a change log"? (see 'listing 4.1')
#   Ongoing: 2023-03-24T22:46:44AEDT a better definition for 'Entity'?
#   Ongoing: 2023-03-24T22:52:57AEDT where do classes defining containers fit into the rule "only entitys should be mutable" (are they entitys/value-objects/other?) ((or) is the book presuming containers aren't the sort of thing one is likely to be defining)
#   Ongoing: 2023-03-24T22:54:31AEDT book "When an object should be immutable" checklist feels *wildly* inadequate
#   Ongoing: 2023-03-25T21:18:10AEDT Java/Oracle Entity definition: says an Entity can be a database table, then later says each row is an entity and there is one entity instance for each row?
#   Ongoing: 2023-03-25T21:20:04AEDT Entity objects -> a Java centric concept from a Java centric book(?)
#   Ongoing: 2023-03-25T21:51:27AEDT comparing custom objects in python requires '__eq__()' to be implemented (otherwise the test is whether they are the same object) [...] (this requirement is still true if using unittest.TestCase 'assertEqual()')
#   Ongoing: 2023-03-25T22:06:37AEDT 'test_moveLeft' -> what is stopping us comparing objects for our mutable-object version test?
#   Ongoing: 2023-03-25T22:28:38AEDT for an instance of a unittest.TestCase class (is there any method which we can call 'runAll()') (besides the command to run all tests in file)
#   Ongoing: 2023-03-25T22:43:54AEDT 'Use internally recorded events to verify changes on mutable objects' -> I'm highly skeptical (this should be a general rule)
#   Ongoing: 2023-03-25T22:55:20AEDT fluent interface -> implies returning the same object, or the same type of object?
#   }}}


#   4.1) Entities: identifiable objects that track change and record events
#   <(has a unique-id)>
#   An application's core objects - These represent important concepts from the business domain
#   They hold relevant data, and may offer ways to manipulate that data
#   Entities are mutable objects
#   Methods that change the entity's state should have no return type, and their names should be in imperative (commanding) form (eg: 'addLine()', 'finalize()'). They should not allow the object to end up in an invalid state.
#   <(Don't expose internals for testing purposes, instead keep a change log and expose that)>
class SalesInvoice:
    def create(salesInvoiceID):
        result = SalesInvoice()
        result.salesInvoiceID = salesInvoiceID
        return result
    def __init__(self):
        self.events = []
        self.finalized = False
        self.salesInvoiceID = None
    def finalize(self):
        self.finalize = True
    def addLine(item):
        if self.finalized:
            raise Exception(f"SalesInvoice is finalized")
        new_line = Line(item)
        self.events.append(new_line)
    def totalNetAmount(self) -> int:
        raise NotImplementedError()
    def totalAmountIncludingTaxes(self) -> int:
        raise NotImplementedError()

#   Entity Objects:
#   {{{

#   LINK: https://stackoverflow.com/questions/695934/is-there-a-difference-between-an-entity-and-a-object
#   An Entity is an abstract concept that's typically represented by a table in a database schema

#   The Java/Oracle definition:
#   LINK: https://docs.oracle.com/cd/B10463_01/web.904/b10390/bc_awhatisaneo.htm#:~:text=Entity%20objects%20are%20classes%20that,%2C%20departments%2C%20sales%2C%20and%20regions
#   LINK: https://docs.oracle.com/cd/A97335_02/apps.102/bc4j/developing_bc_projects/bc_awhatisaneo.htm
#
#   Entity objects are classes that encapsulate the buisness model, including: rules, data, relationships, and persistent behaviour
#   They can represent:
#           The logical structure of the buisness (product lines, departments, sales, and regions)
#           Buisness documents (invoices, change orders, and service requests)
#           Physical items (warehouses, employees, and equipment)
#   An Entity represents an object in the real world domain
#
#   The best place to write buisness logic is in entity objects (to enforce buisness logic for all view of data). Buisness logic includes
#           Rules and policy
#           Validation
#           Deletion
#           Calculations
#           Default values
#           Security
#
#   A common use of entity objects is to represent a database table or some other kind of file (and combine said table with relevent buisness logic)
#   A table may be represented by more than one object
#   <(Each entities objects represents a row, there is only one instance per row)>
#
#   Entity objects are not exposed to clients - data from them is accessed through view objects
#   One entity object can be used by multiple view objects

#   <(The wider accepted definition of an Entity is an object that represents a database table?)>

#   }}}


#   4.2) Value objects: replaceable, anonymous, and immutable values
#   Often small, with just one/two properties
#   Eg: SalesInvoiceID, Date, Quantity, ProductID

#   When transforming a value object, instead of modifying the original object, return a modified copy
#   This effectively makes the object immutable
class Quantity:
    def __init__(self, quantity: int, precision: int):
        self.quantity = quantity
        self.precision = precision
    def fromInt(quantity: int, precision: int):
        return Quantity(quantity, precision)
    def add(self, other: 'Quantity') -> 'Quantity':
        if self.precision != other.precision:
            raise ValueError("precisions must match")
        return Quantity(self.quantity + other.quantity, self.precision)


#   4.3) Data Transfer Objects: simple objects with few design rules
#   (see 03-creating-data-objects)


#   4.4) Prefer immutable objects
#   Most objects that are not entitys should be immutable
#   (this eliminates opportunities for an object to be unexpectedly altered)

#   Replace such objects instead of modifying them.
#   Requires us to use:
#               year = year.next()
#   instead of 
#               year.next()

#   <(When an object should be immutable)>:
#           It is a service object
#           It is a data-object but not an entity
#           <>
#   (in practice there are times when other objects must be mutable, but one should always default to making objects immutable)


#   4.5) A modifier on an immutable object should return a modified copy
class Integer:
    def __init__(self, value: int):
        self.value = value
    def plus(self, other: int) -> Integer:
        return Integer(self.value + other)

x = Integer(5)
x.plus(5)
assert x.value == 5
x = x.plus(5)
assert x.value == 10


#   4.6) On a mutable object, modifier methods should be command methods 
#   Their name should be in imperative form (giving a command)
#   Eg: 'moveLeft()' for modifier method, 'toTheLeft()' for the immutable object method
#   Such methods should have a void return type.


#   4.7) On immutable objects, modifier methods should have declarative names
#   'moveLeft()' is a poor name for a method the must be used like 'x = x.moveLeft()'
#   Use a name of the form "I want this, but"
#   Eg: 'toTheLeft()' or 'withXDecreasedBy()'

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __eq__(self, lhs):
        return (self.x == lhs.x and self.y == lhs.y)
    def moveLeft(self, x: int):
        self.x -= x
    def toTheLeft(self, x: int) -> Position:
        return Position(self.x - x, self.y)


#   4.8) Compare whole objects
#   Comparing elements of objects requires us to expose the internals of the object to the tester
def test_moveLeft():
    p = Position(10, 20)
    p.moveLeft(4)
    assert p.x == 6
#
#   Comparing the test object to a whole separate object allows us to keep internals private
#   (in python, '__cmp__()' must be manually implemented for such a comparison)
def test_toTheLeft():
    p = Position(10, 20)
    p = p.toTheLeft(4)
    assert p == Position(6, 20)
#
test_moveLeft()
test_toTheLeft()
#   <(book states comparing objects is <only?> possible for immutable objects -> (but it's not? why ~~can't~~ shouldn't mutable version test perform the same comparison?))>


#   4.9) When comparing immutable objects, assert equality not sameness
#   Compare objects by-value, not by by-reference
#   (languages differ in how to compare objects - python requires us to implement '__cmp__()')
#   (a custom comparison function should only be implemented if actually needed by tests)


#   4.10) Calling a modifier method should always result in a valid object
#   None of an objects methods should allow the object to end up in an invalid state
#   Such functions should validate their input, and if returning a new object, reuse the default ctor to validate it
class Fraction:
    def __init__(self, numerator: float, denominator: float):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        self.numerator = numerator
        self.denominator = denominator
    def withDenominator(self, newDenominator: float) -> Fraction:
        return Fraction(self.numerator, newDenominator)

class TestFraction(unittest.TestCase):
    def test_Fraction(self):
        f = Fraction(1,2)
        with self.assertRaises(ValueError) as e:
            f = f.withDenominator(0)
        self.assertEqual(str(e.exception), "Denominator cannot be 0")

t = TestFraction()
t.test_Fraction()


#   4.11) A modifier method should verify that the requested state change is valid
#   <(see 4.10?)>
#   Write unit tests to verify invalid state transitions cannot occur


#   4.12) Use internally recorded events to verify changes on mutable objects
#   <>


#   4.13) Don't implement fluent interfaces on mutable objects
#   (recall modifier methods of mutable objects should return void)
#   A fluent interface is when modifier methods return <(type/value)> 'self', allowing chaining of methods
#   Eg:         query = QueryBuilder.create().select(s).from(f).where(w)
#
#   If an object is mutable, there is no immediately obvious correct way to use such methods
#
#   Immutable objects lend themselves towards fluent interfaces, since every modifier method by-definition must return a new instance of the same object


#   Using libraries that do not follow these rules
#   It's usually ok to use such libraries as-is, so long as such use is kept encapsulated
#   contention: it may be a good idea to wrap mutable classes to make them immutable


#   Summary:
#   <(Entity objects typically represent database tables, and are the place for relevant business logic)>
#   <(Entity objects should keep a log of events and expose that to tests, instead of exposing internals)>
#   Always default to making (non-entity) objects immutable
#   Modifier methods for immutable objects should have declarative names and should return a modified copy of the object
#   Modifier methods for mutable objects should have imperative names and return void
#   Modifier methods should always leave the object in a valid state

