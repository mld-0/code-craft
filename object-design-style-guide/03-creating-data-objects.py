#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import math
import re
import unittest
#   Ongoings:
#   {{{
#   Ongoing: 2023-02-23T21:07:39AEDT checking 'lat' / 'long' together or separately, setting one before checking both(?)
#   Ongoing: 2023-02-23T21:11:57AEDT rejecting invalid input - exceptions vs assertions
#   Ongoing: 2023-02-23T21:14:12AEDT python, validating type given to objects, (using 'self.x = float(x)'?)
#   Ongoing: 2023-02-23T21:26:15AEDT Coordinates.__init__() -> calling 'float()' 4 extra times is wasteful (but neater than putting a 'lat = float(lat)' assignment before it?)
#   Ongoing: 2023-02-23T21:29:57AEDT argument validation order (what error message we want to show when the user passes multiple invalid things)
#   Ongoing: 2023-02-23T21:51:41AEDT multiple ctors (with different arguments for different cases) (or worse same number of different arguments) in python -> (a sign we should be using factory functions in any case)
#   Ongoing: 2023-02-23T21:52:34AEDT example 'Line' having different ctors for dotted / solid -> should probably be different types (can't distinguish dotted/solid once they are created with different ctors when they are the same type?)
#   Ongoing: 2023-03-22T22:38:45AEDT (any way to) match exception message when using 'with self.assertRaises(e)'?
#   Ongoing: 2023-03-22T22:53:13AEDT an instance of 'EmailAddress' can only contain an email address that is valid -> (or at least it would in a language that doesn't allow the user to modify any member variable at will)
#   Ongoing: 2023-03-22T22:56:56AEDT should argument to 'User' ctor be a string or an 'EmailAddress' (consider in python types are not enforced) [...] (also requiring 'User(EmailAddress("abc@gmail.com"))' from the client is obnoxious?)
#   Ongoing: 2023-03-22T23:40:56AEDT exercises as examples (this chapter / other chapters)?
#   }}}

#   Continue: 2023-02-23T21:58:14AEDT complete chapter.
#   Continue: 2023-03-22T23:28:53AEDT exceptions vs assertions for validating ctor/function inputs

#   Require data needed to behave consistently:
#   For a position to be valid, it must have x/y values, so we require them in the ctor
#   (Domain invariant: something that is always true for a given object)
class Position:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
    def distanceTo(self, other: 'Position'):
        return math.sqrt( (self.x - other.x) ** 2 + (self.y - other.y) ** 2 )


#   Require data that is meaningful: (reject invalid data)
class Coordinates:
    def __init__(self, lat: float, long: float):
        if not (float(lat) >= -90 and float(lat) <= 90):
            raise ValueError(f"invalid latitude=({lat}), must be [-90,90]")
        if not (float(long) >= -180 and float(long) <= 180):
            raise ValueError(f"invalid longitude=({long}), must be [-180,180]")
        self.lat = float(lat)
        self.long = float(long)


#   Domain rules: at least 1 adult, at least 1 room, no more rooms than there are guests
class ReservationRequest:
    def __init__(self, numRooms: int, numAdults: int, numChildren: int):
        if int(numRooms) != float(numRooms) or int(numAdults) != float(numAdults) or int(numChildren) != float(numChildren):
            raise TypeError("Arguments must be integers")
        if numAdults < 1:
            raise ValueError("Must have at least 1 adult")
        if numChildren < 0:
            raise ValueError("Number of children cannot be negative")
        if numRooms < 1:
            raise ValueError("Must book at least 1 room")
        if numRooms > numAdults + numChildren:
            raise ValueError("Number of rooms must not exceed number of guests")
        self.numRooms = int(numRooms)
        self.numAdults = int(numAdults)
        self.numChildren = int(numChildren)



#   Remove superfluous arguments: 
#   (argument 'total' is redundant, since it must be equal to first + second)
class Deal:
    def __init__(self, first: float, second: float):
        self.first = float(first)
        self.second = float(second)
        self.total = self.first + self.second


#   Use Factory Functions where there are different cases requiring different arguments for the ctor
#   <(bad example?)>
class Line:
    def make_dotted(dot_distance: float) -> 'Line':
        l = Line()
        l.dot_distance = dot_distance
        return l
    def make_solid() -> 'Line':
        l = Line()
        return l


#   Unit-tests for type invariants
class TestCoordinates(unittest.TestCase):
    def test_Coordinates_init_lat_validation(self):
        with self.assertRaises(ValueError):
            c = Coordinates(-91, 0)
        with self.assertRaises(ValueError):
            c = Coordinates(91, 0)
        with self.assertRaises(TypeError):
            c = Coordinates(None, 0)
        with self.assertRaises(ValueError):
            c = Coordinates("", 0)


#   Don't use custom exceptions for invalid arguments:
#   (and don't try to recover from them, terminate the program and fix the function call)

#   There may be a case for custom exceptions for runtime errors we may wish to recover from

#   Unit tests expecting an exception should validate that the correct exception is thrown:
#   (one way to do this without using custom exceptions is to check the exception error message)

#   Extract new objects to prevent domain invariants being verified in multiple places:
#   (consider creating such a type wherever a function accepts a primitive argument which it must validate)
class EmailAddress:
    def __init__(self, emailAddress):
        if not self._isValidEmail(emailAddress):
            raise ValueError(f"invalid email=({emailAddress})")
        self.emailAddress = emailAddress
    def _isValidEmail(self, emailAddress):
        if re.fullmatch(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])", emailAddress):
            return True
        return False
class User:
    def __init__(self, emailAddress: str):
        self.emailAddress = EmailAddress(emailAddress)
    def setEmail(self, emailAddress: str):
        self.emailAddress = EmailAddress(emailAddress)

u = User("abc@gmail.com")


#   Extract new objects to represent composite values:
#   Some types belong together / frequently get passed together
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
class Account:
    def __init__(self, name: str, money: Money):
        self.name = name
        self.money = money
    #   Since passing objects to the ctor can be tedious 
    #           eg: Account("Larry", Money(5700, "GBP"))
    #   create a factory function which receives these values as primitives
    def new(name: str, amount: int, currency: str):
        return Account(name, Money(amount, currency))

a = Account.new("Larry", 5700, "GBP")


#   Assertions vs Exceptions for validating ctor arguments:
#   <(contention: use assertions instead of exceptions?)> ... (is that what the book is even saying?)
#   <(contention: unit tests are not necessary for cases where errors can be prevented by the type system)>
#   {{{
#   <(assertions vs exceptions for validating arguments)>
#   }}}



#   Don't collect exceptions:
#   In general, don't attempt to provide a list of everything that fails validation, simply throw an exception for the first thing to fail, and leave the next exception for when the first invalid value has been corrected.
#   If it is necessary to supply the user with a list of everything wrong with the data they submitted, use a data transfer object (DTO).


#   Don't inject dependencies, optionally pass them as method arguments:
#   <(Service object dependencies should be injected as ctor arguments, however data-objects ctors should only receive primitives or other data-objects, if a data-object needs a service to perform some task, it should be provided as a method argument)>
#   <(rationale?)>
#   <(examples: 3.23/3.24 vs 3.25/3.26 ... 'PasswordHasher'?)>


#   Use named ctors (factory functions):
#   (use the default ctor for service objects, and provide factory functions for data objects)>
#   <(rationale?)>


