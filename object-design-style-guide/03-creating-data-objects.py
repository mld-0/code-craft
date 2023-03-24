#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import math
import re
import datetime
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
#   Ongoing: 2023-03-24T21:04:42AEDT testing an assertion fails (vs testing an exception is thrown)
#   }}}

#   Data objects (or value-objects/entities)

#   3.1) Require the minimum amount of data needed to behave consistently:
#   For a position to be valid, it must have x/y values, so we require them in the ctor
#   (Domain invariant: something that is always true for a given object)
class Position:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
    def distanceTo(self, other: 'Position'):
        return math.sqrt( (self.x - other.x) ** 2 + (self.y - other.y) ** 2 )


#   3.2) Require data that is meaningful: (reject invalid data)
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


#   3.3) Don't use custom exceptions for invalid arguments:
#   (and don't try to recover from them, terminate the program and fix the function call)

#   There may be a case for custom exceptions for runtime errors we may wish to recover from

#   3.4) Unit tests expecting an exception should validate that the correct exception is thrown:
#   (one way to do this without using custom exceptions is to check the exception error message)


#   3.5) Extract new objects to prevent domain invariants being verified in multiple places:
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


#   3.6) Extract new objects to represent composite values:
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


#   3.7) Assertions vs Exceptions for validating ctor arguments:
#   Use Exceptions to validate public function arguments
#   Use Assertions to document program invariants
#   {{{

#   LINK: https://softwareengineering.stackexchange.com/questions/137158/is-it-better-to-use-assert-or-illegalargumentexception-for-required-method-param
#   Takeaway: Use exceptions, not assertions

#   LINK: https://stackoverflow.com/questions/9169691/how-to-check-constructor-arguments-and-throw-an-exception-or-make-an-assertion-i
#   Throwing exceptions in constructors is less than ideal. Whenever I need a type with restrictions on the domains of any of its constructor parameters, I make the constructor private and force instantiation through a factory that applies the constraints and either throws (via require, usually) or returns Try[ConstrainedType]

#   LINK: https://docs.oracle.com/javase/8/docs/technotes/guides/language/assert.html
#   Always consider that assertions may be disabled with a flag
#   Use assertions for:
#           Internal invariants
#                   Something programmers know should be true
#                   (assert it instead of commenting it)
#           Control-Flow invariants
#                   Any place one assumes should never be reached
#                   (assert it instead of commenting it)
#           Validating arguments for non-public functions
#           Validating program invariants
#   Do not use assertions for:
#           Validating arguments for public functions
#           Performing any check required for program correctness
#           Performing any action with side effects

#   LINK: https://stackoverflow.com/questions/1276308/exception-vs-assertion
#   Use assertions for internal logic checks within your code, and normal exceptions for error conditions outside your immediate code's control (Don't forget assertions can be turned off)
#   Unchecked exceptions are designed to detect programming errors of the users of your library, while assertions are designed to detect errors in your own logic
#   Use assertions for any validation that is slow
#   Assertions are for verifying invariants
#   Use exceptions for conditions you expect to occur, and user assertions for conditions that should never occur

#   }}}


#   Don't collect exceptions:
#   In general, don't attempt to provide a list of everything that fails validation, simply throw an exception for the first thing to fail, and leave the next exception for when the first invalid value has been corrected.
#   If it is necessary to supply the user with a list of everything wrong with the data they submitted, use a data transfer object (DTO).


#   3.8) Don't inject dependencies, optionally pass them as method arguments:
#   <(Service object dependencies should be injected as ctor arguments, however data-objects ctors should only receive primitives or other data-objects, if a data-object needs a service to perform some task, it should be provided as a method argument)>
#   <(rationale?)>
#   <(examples: 3.23/3.24 vs 3.25/3.26)>
#   {{{

def _3_23():
    class Money:
        def __init__(self, amount: int, currency: Currency):
            self.amount = amount
            self.currency = currency
        def convert(self, exchangeRateProvider: ExchangeRateProvider, targetCurrency: Currency) -> 'Money':
            exchangeRate = exchangeRateProvider.getRateFor(self.currency, targetCurrency)
            return exchangeRate * self.amount


#   Doesn't use 'ExchangeRateProvider' (require 'Money' to expose its 'amount/currency variables)
def _3_24():
    class ExchangeRate:
        def __init__(self, currencyFrom: Currency, currencyTo: Currency, rate: float):
            self.currencyFrom = currencyFrom
            self.currencyTo = currencyTo
            self.rate = rate
        def convert(amount: int) -> 'Money':
            return Money(amount * self.rate, currencyTo)

    #exchangeRateProvider = ...
    money = Money(53, Currency("AUD"))
    exchangeRate = exchangeRateProvider.getRateFor(money.currency, Currency("GBP"))
    result = exchangeRate.convert(money.amount)

#   Pass 'ExchangeRate' instead of 'ExchangeRateProvider'
def _3_25():
    class Money:
        def __init__(self, amount: int, currency: Currency):
            self.amount = amount
            self.currency = currency
        def convert(exchangeRate: ExchangeRate) -> 'Money':
            assert self.currency == exchangeRate.fromCurrency()
            return Money(exchangeRate.rate * self.amount, exchangeRate.currencyTo)

    #exchangeRateProvider = ...
    money = Money(53, Currency("AUD"))
    exchangeRate = exchangeRateProvider.getRateFor(money.currency, Currency("GBP"))
    result = money.convert(exchangeRate)

#   Define new service class 'ExchangeService'
def _3_26():
    class ExchangeService:
        def __init__(self, exchangeRateProvider: ExchangeRateProvider):
            self.exchangeRateProvider = exchangeRateProvider
        def convert(money: Money, targetCurrency: Currency) -> 'Money':
            exchangeRate = exchangeRateProvider.getRateFor(money.currency, targetCurrency)
            return Money(money.amount * exchangeRate, targetCurrency)

    #exchangeRateProvider = ...
    money = Money(53, Currency("AUD"))
    exchangeService = ExchangeService(exchangeRateProvider)
    result = exchangeService.convert(money, Currency("GBP"))


#   Comparing 3.23/3.24/3.25/3.26:
#   <>

#   }}}

#   <(example: exercise 'PasswordHasher')>
#   {{{
#   }}}


#   3.9) Use named ctors (factory functions):
#   (use the default ctor for service objects, and provide factory functions for data objects)>
#   <(rationale?)>

#   The constructor can be made private to force clients to use factory functions

class Date:
    def __init__(self):
        self.format = 'd/m/Y'
        self.date = None
    def fromString(date: str) -> 'Date':
        result = Date()
        result.date = datetime.datetime.fromisoformat(date)

#   Don't immediately create symmetrical 'toString()' method (without being sure of the need for it)

#   Factory functions <can/should> use names from the problem domain
class SalesOrder:
    def __init__(self):
        ...
    def place() -> 'SalesOrder':
        result = SalesOrder()
        ...
        return result

#   domain invariants common to multiple factory functions <can/should> be enforced by ctor
class NaturalNumber:
    def __init__(self, value):
        assert value > 0
        self.value = value
    def fromInt(value: int) -> 'NaturalNumber':
        return NaturalNumber(value)
    def fromFloat(value: float) -> 'NaturalNumber':
        return NaturalNumber(int(value))


#   3.10) Don't use property filters
#   (a property filler method looks like 'fromArray')
class Position:
    def __init__(self):
        self._x = None
        self._y = None
    def fromArray(data: Dict[int]) -> 'Position':
        result = Position()
        result._x = data['x']
        result._y = data['y']
        return result
#   <(the object's internals are now out in the open, make sure the construction of an object always happens in a way that's fully controlled by the object itself ... (so what is the problem here?))>



#   3.11) Don't put anything more into an object than it needs
#   If one doesn't know what data will be needed by a class, declare the class without member variables and only add them as needed


#   3.12) Don't test valid ctor behaviour
#   The only tests that should be written for a ctor are for invalid arguments to ensure that they are rejected correctly
#   Creating other tests for ctors can lead to the premature addition of unneeded ctor arguments
#   Writing tests for the desired behaviour of an object is a better way to establish what data is needed at construction time and what can be provided later
#   Validating that an object has been constructed successfully can lead to member variables being unnecessarily exposed 


#   3.13) Data transfer objects (DTOs) (the exception to the rule)
#           Empty ctor
#           Member variables are public (can be set one-by-one)
#           Member variables are only primitive types (or other DTOs)
#   Used to collect/contain data coming from outside the application
#   With public variables there is no need for getters/setters
#   Provide a 'validate()' method (which returns a list of all errors instead of throwing an exception at the first one)
#   Can provide a factory function if appropriate (which can also perform validation)



#   Summary:
#           Data-objects receive values, not dependencies. On construction, they should receive only the minimum amount of data in order to behave consistently. (Don't pass service-objects to data-object ctors). Ctors should throw an exception if arguments are invalid in some way.
#           Wrap primitive type arguments inside data-objects. Use this to combine related values. These objects should not be able to be constructed with invalid data. Use a domain-specific name for these classes.
#           Use factory functions with domain-specific names for data objects instead of defining multiple ctors for different sorts of arguments.
#           Don't provide any more data to a ctor than is needed 
#           A Data-Transfer-Object (DTO) is a class with all-public member variables, which does not typically follow these rules

