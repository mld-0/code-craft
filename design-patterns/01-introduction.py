#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import math

#   Ongoings:
#   {{{
#   2023-08-21T20:22:29AEST so far in the introduction, they have stated that most techniques given here use inheritance in some form ... then go-on to restate (calling it the 'second principle of OO design': "Favour object composition over class inheritance") ... (do we need some item on when inheritance is in-fact called for (square that with Rust's efforts to discourage traditional inheritance?)) 
#   2023-08-21T20:32:31AEST if the second principle of OO design is "prefer composition over inheritance" - what was the first (that we missed?)
#   2023-08-21T22:32:57AEST dynamic binding (virtual functions?) ... as opposed to static binding (which is inheritance?)
#   2023-08-22T20:48:59AEST in the context of a 'Builder' what is meant by 'representation'?
#   2023-08-22T20:52:10AEST plz revisit 'Brief Descriptions' (of each design pattern) upon completion of <article/items> for each
#   2023-08-22T21:19:59AEST rephrase the 'variable:' definition (and update the definitions accordingly) (again, upon completion of <article/items> for each) [...] (and do a sanity-check that these definitions (and the definition-definitions) actually correspond with the write patterns)
#   2023-09-01T20:05:57AEST elaborate on tight vs loose coupling
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


#   Brief Descriptions:
#   (Creational)
#   Abstract Factory: 
#       an interface for creating families of objects without specifying their concrete class
#       variable: families of product objects
#   Builder: 
#       separate construction of object from its representation (allowing the same process to create different representations)
#       variable: how a composite object gets created
#   Factory Method: 
#       interface for creating objects that allows subclasses decide which class to instantiate
#       variable: the subclass of the object instantiated
#   Prototype: 
#       create new objects according to the type of a supplied 'prototype' object
#       variable: the class of the object instantiated
#   Singleton: 
#       ensure a class has only one instance, and provide a global point of access to it
#       variable: the sole instance of a class
#
#   (Structural)
#   Adapter: 
#       convert the interface of a class into another interface the client is expecting
#       variable: the interface to an object
#   Bridge: 
#       decouple an abstraction from its implementation
#       variable: the implementation of an object
#   Composite: 
#       compose objects into tree structures to represent hierarchies (allows clients to treat compositions of objects uniformly)
#       variable: the structure and composition of an object
#   Decorator: 
#       attach additional responsibilities to objects dynamically (flexible alternative to subclassing)
#       variable: responsibilities of an object without subclassing
#   Facade: 
#       provide a unified interface to a set of subsystem interfaces
#       variable: our interface to a subsystem
#   Flyweight: 
#       use sharing to support large numbers of fine-grained objects efficiently
#       variable: storage costs of objects
#   Proxy: 
#       placeholder for another object to control access to it
#       variable: an object is accessed; it's location
#
#   (Behavioural)
#   Chain of Responsibility: 
#       allow multiple objects a chance to handle the sender's request
#       variable: the objects that can fulfill a request
#   Command: 
#       encapsulate a request an object (allowing <>)
#       variable: when and how a request is fulfilled
#   Interpreter: 
#       a representation for a language's grammar, interpretor for that language
#       variable: grammar and interpretation of a language
#   Iterator: 
#       provide access to elements of an underlying object sequentially
#       variable: how an aggregate's elements are accessed, traversed
#   Mediator: 
#       object which encapsulates how a set of objects interact (promoting loose coupling)
#       variable: how and which objects interact with each other
#   Memento: 
#       capture/save/restore an object's internal state (without violating encapsulation)
#       variable: what private information is stored outside an object, and when
#   Observer: 
#       notify/update all dependencies of an object when that object changes
#       variable: which objects depend on another; how the dependent objects stay up-to-date
#   State: 
#       allow an object to change behaviour (appear to change class) when it's internal state changes
#       variable: [{states of an object}]
#   Strategy: 
#       encapsulate a family of algorithms, making them interchangeable
#       variable: [{our choice of}] <an> algorithm
#   Template Method: 
#       define an operation as class, with each step as a separate method, optionally delegating implementations to subclasses
#       variable: steps of an algorithm (per subclass)
#   Visitor: 
#       define a new operation on an existing class, without changing said class
#       variable: operations applicable to an object (without changing it's class)


#   How Design Patterns solve Design Problems
#
#   Finding Appropriate Objects:
#   OO design can be difficult and lead to classes that have no counterpart in the real world
#   Design patterns can help identify less-obvious abstractions and the objects that can capture them
#
#   Determining object granularity:
#   Several design patterns help with this problem:
#       - Facade describes how to represent complete systems as objects
#       - Flyweight describes how to support large numbers of objects at the finest granularities
#       - Abstract Factory and Builder describe objects for creating other objects
#       - Visitor/Command describe objects which implement requests for another object
#
#   Specifying object interfaces:
#   Methods define operations an object may perform.
#   A methods signature is defined by its name, parameters, and return value [{and scope?}]
#   An objects interface is the set of signatures it makes available to perform operations
#   An object is a subtype of an another if its interface contains the interface of that supertype

#   Dynamic binding: (polymorphism) use of different objects supporting the same interface interchangeably, with the implementation to call being determined at runtime



#   Specifying object implementations:
#   An objects implementation is defined by its class (which specifies representation, internal data, and operations)
#   Objects are created by instantiating a class, creating an instance of that class.

#   OMT notation: 
#   {{{
#   (see pg 15)
#           instance of: dashed arrow 
#           subclass of: vertical line w/ triangle
#           implementation: dog-eared box connected by dashed line
#   }}}


#   Abstract classes are classes that cannot be instantiated, they provide common interfaces, by delegating some or all of their functionality to derived classes
#
#   Concrete classes are classes with no abstract methods
#
#   Mixin class: a class which is intended to provide an additional interface to an existing derived class through multiple inheritance
#   {{{
class Parent:
    def hello(self):
        return "Hello World"
class Mixin:
    def goodbye(self):
        return "Goodbye"
class AugmentedChild(Parent, Mixin):
    ...
def test_AugmentedChild():
    ac = AugmentedChild()
    assert ac.hello() == "Hello World"
    assert ac.goodbye() == "Goodbye"
test_AugmentedChild()
#   }}}


#   Class versus Interface and Inheritance:
#   An objects class defines its implementation
#   An objects type defines its interface
#   [{some languages make this distinction regarding inheritance}]
#
#   Program to an interface, not an implementation:
#   [{Polymorphism depends on interface sharing via inheritance}]
#   Benefits of manipulating objects solely in terms of abstract interfaces:
#       -   Clients remain unaware of the specific types and implementations of the objects they use, as long as those objects all adhere to the interface
#   <>
#   See: Abstract Factory, Builder, Factory Method, Prototype, and Singleton


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


#   Parameterized (Generic) Types: `vec<T>`
#   (Templates) Use of a variable type parameter
#   A powerful third alternative to class-inheritance/object-composition


#   Relating runtime/compile-time structures: aggregation vs acquaintance
#   The runtime structure of a program can vary wildly from it's code structure
#       -   Aggregation: one object owns or is responsible for another
#       -   Acquaintance: one object knows of another object
#   The relationship between aggregation and acquaintance is defined by the rules of the language being used
#   Composite and Decorator are patterns useful for building complex run-time structures.
#   Observer runtime patterns are often hard to understand without knowing the pattern.
#   Chain of Responsibility results in communication patterns that inheritance doesn't reveal.


#   Designing for change: Common causes of redesign, with relevant Design Patterns
#   Good use of design patterns makes systems more robust to particular kinds of change.
#
#   1)  Creating an object by specifying a class explicitly: 
#       Specifying a class name when creating an object commits one to a particular implementation instead of a particular interface. To avoid it, create objects indirectly. 
#       See: Abstract Factory, Factory Method, Prototype
#
#   2)  Dependence on specific operations:
#       Specifying a particular operation commits to it. [{Avoid hard-coded requests}].
#       See: Chain of Responsibility, Command
#
#   3)  Dependence on hardware and software:
#       [{Design systems to limit platform dependencies}]
#       See: Abstract Factory, Bridge
#
#   4)  Dependence on object representation/implementation
#       [{Hiding implementation details from clients keeps changes from cascading}]
#       See: Abstract Factory, Bridge, Memento, Proxy
#
#   5)  Algorithmic dependencies
#       Isolate any algorithms that are likely to need to be changed.
#       See: Builder, Iterator, Strategy, Template Method, Visitor
#
#   6)  Tight Coupling
#       Loose coupling makes it easier to change individual classes, and increases their re-usability 
#       See: Abstract Factory, Bridge, Chain of Responsibility, Command, Facade, Mediator, Observer
#
#   7)  Extending functionality through subclassing
#       Subclassing often requires knowledge of the workings of the parent class, especially where methods need to be overridden. Composition can be a more flexible alternative - although it also adds complexity to designs that can make them harder to understand.
#       See: Bridge, Chain of Responsibility, Composite, Decorator, Observer, Strategy
#
#   8)  Inability to alter classes continently
#       Sometimes it is infeasible to change a class, either because it is part of a wider, more complicated design, or because the source code is not available. 
#       See: Adapter, Decorator, Visitor


#   Application programs, toolkits, and frameworks:
#   Internal reuse, maintainability, and extension are generally high priorities, which design-patterns can facilitate. 
#
#   Toolkits: classes from libraries meant to provide useful functionality (the OO equivalent of a subroutine library).
#   <>
#
#   Frameworks: a set of cooperating classes that make a reusable design for specific software.
#   <>


#   How to select a Design Pattern:
#       1)  Consider how each design pattern solves design problems
#       2)  Scan 'Intent' sections for each pattern
#       3)  Study how patterns interrelate (see Figure 1.1, pg 12)
#       4)  Study patterns of like purpose (pg 79)
#       5)  Examine a case of redesign (pg 24)
#       6)  Consider what should be variable in the design (see Table 1.2, or descriptions above)


#   How to use a Design Pattern:
#       1)  Read the pattern once for an overview
#       2)  Study the 'Structure', 'Participants', and 'Collaborations' sections
#       3)  Look at the sample code section
#       4)  Chose names for the pattern participants that are meaningful in the application context
#       5)  Define the classes
#       6)  Define application-specific names for operations in the pattern
#       7)  Implement the operations to carry out the responsibilities and collaboration in the pattern


