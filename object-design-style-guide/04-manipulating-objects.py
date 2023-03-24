#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import sys
import os
import unittest
#   Ongoings:
#   {{{ 
#   Ongoing: 2023-03-24T22:29:59AEDT does 'entity' imply "has a change log"? (see 'listing 4.1')
#   Ongoing: 2023-03-24T22:46:44AEDT a better definition for 'Entity'?
#   Ongoing: 2023-03-24T22:52:57AEDT where do classes defining containers fit into the rule "only entitys should be mutable" (are they entitys/value-objects/other?) ((or) is the book presuming containers aren't the sort of thing one is likely to be defining)
#   Ongoing: 2023-03-24T22:54:31AEDT book "When an object should be immutable" checklist feels *wildly* inadequate
#   }}}


#   4.1) Entities: identifiable objects that track change and record events
#   <(has a unique-id)>
#   An application's core objects - These represent important concepts from the business domain
#   They hold relevant data, and may offer ways to manipulate that data
#   Entities are mutable objects
#   Methods that change the entity's state should have no return type, and their names should be in imperative (commanding) form (eg: 'addLine()', 'finalize()'). They should not allow the object to end up in an invalid state.
#   <(Don't expose internals for testing purpouses, instead keep a change log and expose that)>
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


#   4.2) Value objects: replaceable, anonymous, and immutable values
#   Often small, with just one/two properties
#   Eg: SalesInvoiceID, Date, Quantity, ProductID

#   When transforming a value object, instead of modifying the origional object, return a modified copy
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
#   (this eliminates opertunities for an object to be unexpectedly altered)
#   Replace such objects instead of modifying them.

#   <(When an object should be immutable)>:
#           It is a service object
#           It is a data-object but not an entity

#   4.5) A modifier on an immutable object should return a modified copy
#   <>


#   4.6) On a mutable object, modifier methods should be command methods
#   <>


#   4.7) On immutable objects, modifier methods should have declarative names
#   <>


#   4.8) Compare whole objects
#   <>


#   4.9) When comparing immutable objects, assert equality not sameness
#   <>


#   4.10) Calling a modifier method should always result in a valid object
#   <>


#   4.11) A modifier method should verify that the requested state change is valid
#   <>


#   4.12) Use internally recorded events to verify changes on mutable objects
#   <>


#   4.13) Don't implement fluent interfaces on mutable objects
#   <>


#   Summary:
#   <>

