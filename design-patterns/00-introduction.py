#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import math

#   Ongoings:
#   {{{
#   2023-08-21T20:22:29AEST so far in the introduction, they have stated that most techniques given here use inheritance in some form ... then go-on to restate (calling it the 'second principle of OO design': "Favour object composition over class inheritance") ... (do we need some item on when inheritance is in-fact called for (square that with Rust's efforts to discourage traditional inheritance?)) 
#   2023-08-21T20:32:31AEST if the second principle of OO design is "prefer composition over inheritance" - what was the first (that we missed?)
#   }}}

#   A Design Pattern has 4 elements:
#       - Name
#       - Problem: when to apply the pattern
#       - Solution: elements that make up the design, their relationships, responsibilities, and collaborations
#       - Consequences: results and trade-offs of applying the pattern


#   Design patterns table:
#                       Purpose
#                       Creational:             Structural:                 Behavioural:
#
#   Scope   Class:      Factory Method          Adapter (class)             Interpreter
#                                                                           Template Method
#   
#           Object:     Abstract Factory        Adapter (object)            Chain of Responsibility
#                       Builder                 Bridge                      Command
#                       Prototype               Composite                   Iterator
#                       Singleton               Decorator                   Mediator
#                                               Facade                      Memento
#                                               Flyweight                   Observer
#                                               Proxy                       State
#                                                                           Strategy
#                                                                           Visitor

#   Aspects that we can vary:
#
#   Abstract Factory                families of product objects
#   Builder                         how a composite object gets created
#   Factory Method                  subclass of object that is instantiated
#   Prototype                       class of object that is instantiated
#   Singleton                       the sole instance of a class
#   
#   Adapter                         interface to an object
#   Bridge                          implementation of an object
#   Composite                       structure and composition of an object
#   Decorator                       responsibilities of an object without subclassing
#   Facade                          interface to a subsystem
#   Flyweight                       storage costs of objects
#   Proxy                           how an object is accessed; its location
#   
#   Chain of Responsibility         object that can fulfill a request
#   Command                         when and how a request is fulfilled
#   Interpreter                     grammar and interpretation of a language
#   Iterator                        how an aggregate's elements are accessed, traversed
#   Mediator                        how and which objects interact with each other
#   Memento                         what private information is stored outside an object, and when
#   Observer                        number of objects that depend on another object; how the dependent objects stay up to date
#   State                           states of an object
#   Strategy                        an algorithm
#   Template Method                 steps of an algorithm
#   Visitor                         operations that can be applied to object(s) without changing their class(es)



#   How Design Patterns solve Design Problems
#
#   Finding appropriate objects:
#   <>
#
#   Determining object granularity:
#   <>
#
#   Specifying object interfaces:
#   <>
#   
#   Specifying object implementations:
#   <>


#   Inheritance vs Composition:
#       - The two most common forms of reusing functionality in OO design
#       - White box reuse: inheritance (the internals of the parent are visible to subclasses)
#               - Defined statically at compile-time, (therefore straightforward to use)
#               - Easier to modify implementation being reused
#               - Can't change implementation at runtime
#               - Inheritance breaks encapsulation (changes to parent class may break subclasses)
#       - Black box reuse: composition (only public interface of the class are visible to the user)
#               - Defined dynamically at runtime
#               - Requires classes to respect each other's interfaces
#               - Keeps encapsulation (fewer dependencies)
#               - Easier to manage
#       - Prefer composition over inheritance


#   Delegation:
#   [{A technique for making composition as powerful as inheritance}]
#   A receiving object delegates operations to its delegate (as a subclass might defer requests to its parent class)
#   The receiver passes itself to the delegate
#
#   Eg: A class `Window` uses (delegates) functionality to a `Rectangle` instance variable instead of inheriting from it:
#   {{{
#   (this design allows us to change the 'shape' of the window by changing the type of the member variable, instead of having to derive from a different shape)
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2

class Window:
    def make_rectangular(h, w):
        return Window(Rectangle(h, w))
    def make_circular(r):
        return Window(Circle(r))
    def __init__(self, shape):
        self.shape = shape
    def area(self):
        return self.shape.area()

def test_Window_area():
    w = Window.make_rectangular(5, 3)
    c = Window.make_circular(4)
    assert w.area() == 15
    assert c.area() == math.pi * 4 * 4

test_Window_area()
#   }}}


#   Parameterized Types:
#   Use of a variable type parameter
#   A powerful third alternative to class-inheritance/object-composition


#   Relating runtime/compile-time structures
#   [{aggregation vs acquaintance}]
#   <>


#   Common causes of redesign, with relevant Design Patterns:
#   1)  Creating an object by specifying a class explicitly: Specifying a class name when creating an object commits one to a particular implementation instead of a particular interface. To avoid it, create objects indirectly. See: Abstract Factory, Factory Method, Prototype
#   2)  


#   Application programs, toolkits, and frameworks:
#   <>


#   How to select a Design Pattern:
#   <>


#   How to use a Design Pattern:
#       1) Read the pattern once for an overview
#       2) Study the 'Structure', 'Participants', and 'Collaborations' sections
#       3) Look at the sample code section
#       4) Chose names for the pattern participants that are meaningful in the application context
#       5) Define the classes
#       6) Define application-specific names for operations in the pattern
#       7) Implement the operations to carry out the responsibilities and collaboration in the pattern


