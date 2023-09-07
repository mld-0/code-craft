#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
from abc import ABC, abstractmethod
import copy
#   Ongoings:
#   {{{
#   2023-09-05T21:26:11AEST (when discussing uses-cases) (it seems like we should talk more about when it's convenient to be able to deep-copy objects) (and when it's beneficial to have objects which inherit an interface which declares them to be deep-copyable (and aren't there more modern ways of denoting an object thus?)) [...] (when can we delegate `clone()` to the language we are using instead of using a `Prototype` interface?) ... (and wouldn't `Cloneable` be a better name for that interface?) [...] (in python specifically, what can't `copy.deepcopy()` handle? Can we check if it fails to make an actually deep copy?)
#   2023-09-05T21:48:24AEST Prototype hides product classes from the client ... does it though? (in our example, the client is still responsible for creating the prototype instance of each concrete class) [...] gpt4 suggests a `PrototypeManager` class - providing the client with an instance of each class so they can use `clone()` (presumably instead of ctors) to create new instances?
#   2023-09-07T21:14:44AEST Prototypes and object composition - having member variable classes also implement `clone()`? (should we have everything inherit Prototype? How can we enforce that every member variable type can be deep-copied?)
#   2023-09-07T21:56:56AEST necessity of the `memo[id(self)]` <pattern> when implementing `__deepcopy__()` ourselves?
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
    def __init__(self):
        self.prototypes = dict()
    def register(self, key: str, prototype: Prototype):
        self.prototypes[key] = prototype
    def create_clone(self, key: str) -> Prototype:
        return self.prototypes[key]

def get_manager():
    manager = PrototypeManager()
    manager.register('UNIT_RED_SQUARE', Square(0, 0, "red", 1))
    manager.register('UNIT_BLUE_CIRCLE', Circle(0, 0, "blue", 1))
    return manager

def client():
    manager = get_manager()
    square_1 = manager.create_clone('UNIT_RED_SQUARE')
    circle_1 = manager.create_clone('UNIT_BLUE_CIRCLE')
    print(square_1)
    print(circle_1)
    square_2 = square_1.clone()
    circle_2 = circle_1.clone()

client()


#   (Python) Alternative to inheritance from Prototype:
#   [{implement `def __deepcopy__(self)`, check whether it's implemented with `hasattr(obj, '__deepcopy__')`?}]
#   {{{
#def __deepcopy__(self, memo=None):
#    if memo is None:
#        memo = {}
#
#    # Check if object is already in memo
#    if id(self) in memo:
#        return memo[id(self)]
#
#    # If not, create a new object and add it to the memo
#    new_obj = self.__class__.__new__(self.__class__)  # create a new instance without calling __init__
#    memo[id(self)] = new_obj  # add the new object to the memo
#
#    # Copy the object's attributes
#    for key, value in self.__dict__.items():
#        setattr(new_obj, key, deepcopy(value, memo))
#
#    return new_obj
#   }}}
#   <>


#   [{Collaborations}]:
#   A client asks [{an object implementing Prototype}] to clone itself
#   [{A client asks a PrototypeManager to return a clone}]


#   Consequences:
#   [{The Prototype pattern hides concrete product classes from the client(?)}]
#   <>
#
#   1)  Adding and removing products at run-time
#   [{Prototypes let you incorporate a new concrete product class into a system simply by registering a prototypical instance with the client. That's a bit more flexible than other creational patterns, because a client can install and remove prototypes at run-time}]
#
#   2)  Specify new objects by varying values
#   We can [{define/configure}] a new 'type' by creating a cloneable object with specific variable values, and create new instances of that 'type' by cloning it.
#   [{this can reduce the number of classes a system needs}]
#
#   3)  Specify new objects by varying structure
#   [{how does this vary from (2)?}]
#   <>
#   
#   4)  Reduce subclassing
#   Unlike Factory Method, with Prototype we don't need a hierarchy of Creator/Factory classes paralleling the our hierarchy of Product objects. 
#   [{It is particularly beneficial in languages where classes are not first class objects (that is, where we cannot assign a class type as a variable)}]
#
#   5)  Configure an application with classes dynamically
#   [{The Prototype pattern can be used where a class constructor is not available because the class is loaded dynamically, in this case, asking a PrototypeManager to clone that class becomes our substitute for it's constructor}]
#
#   6)  Cloneability of composite objects
#   The Prototype pattern requires each subclass [{and all it's member variables}] implement `clone()` (deep-copy), which may not always be possible}].
#   <>


#   Implementation:
#   The Prototype pattern is particularly useful in languages like C++, where class are not objects (first class citizens - we cannot store a class type as a variable/parameter).
#
#   1)  Using a PrototypeManager:
#   Provides a registry of all available prototypes [{particularly useful where there is not a fixed number of prototype objects, or we want to shield them from the client}]
#   A PrototypeManager makes a list available to clients of objects they can create by cloning
#
#   2)  Implement the Clone operation
#   Implementing deep-copy correctly can be problematic for some types.
#   How shallow vs deep copy is handled varies by language.
#   [{Some languages may be able to implement clone for us}]
#
#   3)  Initializing clones
#   Having a `clone()` implementation which accepts parameters precludes a uniform 
#   If a client needs to configure an object immediately after cloning it, it may be a better option to instead provide operations to (re-)set part of that objects state which the client can call immediately after creating the cloned object. 


#   Example: MazePrototypeFactory
#   <>


#   Related Patterns:
#   Prototype and Abstract Factory are competing patterns in many ways (although they can be used together - an Abstract Factory might be implemented as a PrototypeManager)
#   Design that make heavy use of the Composite and Decorator patterns often benefit from Prototype

