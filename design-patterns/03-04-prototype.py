#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
from abc import ABC, abstractmethod
import copy
#   Ongoings:
#   {{{
#   2023-09-05T21:26:11AEST (when discussing uses-cases) (it seems like we should talk more about when it's convenient to be able to deep-copy objects) (and when it's beneficial to have objects which inherit an interface which declares them to be deep-copyable (and aren't there more modern ways of denoting an object thus?))
#   2023-09-05T21:48:24AEST Prototype hides product classes from the client ... does it though? (in our example, the client is still responsible for creating the prototype instance of each concrete class) [...] gpt4 suggests a `PrototypeManager` class - providing the client with an instance of each class so they can use `clone()` (presumedly instead of ctors) to create new instances?
#   }}}

#   Pattern: Prototype

#   Intent:
#   Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype

#   Motivation:
#   <>

#   Use the Prototype pattern when:
#   A system should be independent of how its products are created, composed, and represented, along with one or more of the following:
#       -   When the classes to be instantiated are specified at runtime
#       -   To avoid building a hierarchy of factory classes paralleling the hierarchy of Product classes
#       -   When instances of a class can have only one of a few different combinations of state


#   Structure:
class Prototype(ABC):
    """Declares an interface that can clone (deep-copy) itself"""
    @abstractmethod
    def clone(self) -> Prototype:
        raise NotImplementedError()

class Shape(Prototype):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def __repr__(self):
        return f"Shape=({self.__class__.__name__}): position=({self.x}, {self.y})"

class Square(Shape):
    def __init__(self, x, y, color, length):
        super().__init__(x, y, color)
        self.length = length
    def __repr__(self):
        return f"{super().__repr__()}, length=({self.length})"
    def clone(self) -> Square:
        return copy.deepcopy(self)

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius
    def __repr__(self):
        return f"{super().__repr__()}, radius=({self.radius})"
    def clone(self) -> Circle:
        return copy.deepcopy(self)

class PrototypeManager:
    ...

#def client():
#    prototype_square = Square(3, 4, "red", 5)
#    cloned_square = prototype_square.clone()
#    print(cloned_square)
#    prototype_circle = Circle(1, 2, "blue", 3)
#    cloned_circle = prototype_circle.clone()
#    print(cloned_circle)
#
#client()


#   [{Collaborations}]:
#   A client asks [{an object implementing Prototype}] to clone itself


#   Consequences:
#   [{The Prototype pattern hides concrete product classes from the client(?)}]
#   <>
#
#   1)  Adding and removing products at run-time
#   [{Prototypes let you incorporate a new concrete product class into a system simply by registering a prototypical instance with the client. That's a bit more flexible than other creational patterns, because a client can install and remove prototypes at run-time}]
#
#   2)  Specify new objects by varying values
#



