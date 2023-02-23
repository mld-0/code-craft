#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import math
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
#   }}}

#   Continue: 2023-02-23T21:58:14AEDT complete chapter.

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


#   Testing invariants
class TestPosition(unittest.TestCase):
    def test_Position_init_x_validation(self):
    #   {{{
        with self.assertRaises(TypeError):
            p = Position()
        with self.assertRaises(TypeError):
            p = Position(0)
        with self.assertRaises(TypeError):
            p = Position(None, 0)
        with self.assertRaises(ValueError):
            p = Position("", 0)
    #   }}}
class TestCoordinates(unittest.TestCase):
    def test_Coordinates_init_lat_validation(self):
    #   {{{
        with self.assertRaises(ValueError):
            c = Coordinates(-91, 0)
        with self.assertRaises(ValueError):
            c = Coordinates(91, 0)
        with self.assertRaises(TypeError):
            c = Coordinates(None, 0)
        with self.assertRaises(ValueError):
            c = Coordinates("", 0)
    #   }}}
class TestReservationRequest(unittest.TestCase):
    def test_ReservationRequest_init_validation(self):
    #   {{{
        with self.assertRaises(ValueError):
            r = ReservationRequest(0, 1, 1)
        with self.assertRaises(ValueError):
            r = ReservationRequest(1, 0, 1)
        with self.assertRaises(ValueError):
            r = ReservationRequest(1, 0, 0)
        with self.assertRaises(TypeError):
            r = ReservationRequest(None, 0, 0)
        with self.assertRaises(ValueError):
            r = ReservationRequest("", 0, 0)
    #   }}}


#   Remove superfluous arguments: 
#   (argument 'total' is redundant, since it must be equal to first + second)
class Deal:
    def __init__(self, first: float, second: float):
        self.first = float(first)
        self.second = float(second)
        self.total = self.first + self.second


#   <(Use Factory Functions where there are different cases with different arguments for the ctor)>
#   {{{
#   <(bad example?)>
class Line:
    def make_dotted(dot_distance: float) -> 'Line':
        l = Line()
        l.dot_distance = dot_distance
        return l
    def make_solid() -> 'Line':
        l = Line()
        return l
#   }}}


#   Don't use custom exception classes for invalid arguments:



