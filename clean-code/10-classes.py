#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from abc import ABC, abstractmethod

#   Ongoing:
#   {{{
#   2023-08-09T16:02:43AEST functions should follow the stepdown rule -> implying we shouldn't put all public functions before all private ones(?)
#   2023-08-09T16:05:51AEST guidelines for putting utility private methods in a utility/helper class instead of cluttering the class - when/whether we consider private methods to be adding the size of a class (which we have defined as a count of its responsibilities)
#   2023-08-09T16:33:50AEST lessons from the `Sql` class before/after case study ... how the `Where` / `ColumnsList` class fall into implementation ... how to reconcile use of inheritance with the ((strongly) prefer composition over inheritance) principle? [...] (the Open/Closed principle implies the use of inheritance?)
#   2023-08-09T17:26:47AEST interface classes and private methods, interface classes and providing <default/mandatory> implementations
#   2023-08-09T17:34:12AEST Liskov Substitution principle - governs design of base/derived classes, design of functions receiving base/derived objects (or both)
#   2023-08-09T19:42:49AEST applying the interface segregation principle to inheritance from non-interface classes
#   2023-08-09T19:53:45AEST single responsibility principle - how to know when the purpouse of a class includes an 'and' - consider the `ReportGenerator` example, it is easily possible to come up with a definition "create a report" instead of the "generate the contents of a report and output it in the desired format" that suggests it needs to be split into multiple classes(?)
#   2023-08-09T19:56:31AEST other topics related to the single responsibility principle (by wikipedia): GRASP, seperation of concerns, and the chain of responsibility pattern
#   2023-08-09T20:17:12AEST BasicCoffeeMachine/FancyCoffeeMachine example - the use of interface classes allows us to use either in a typed language - what purpouse does this serve in a dynamic language like python(?) [...] which of the SOLID principles talks about the need for interface classes(?) [...] we can write a function dependent on ICoffeeMachine instead of on BasicCoffeeMachine/FancyCoffeeMachine(?) [...] (in this example, presumedly `BasicCoffeeMachine` is the low-level module, the high level module is whatever calls it, and `ICoffeeMachine` is neither the high-or-low level module but instead the talked-about abstraction between them?)
#   2023-08-09T20:20:38AEST dependency injection (as opposed to dependency inversion)(?)
#   }}}

#   The Java convention is to begin a class with a list of variables
#   Public static constants come first, then private static variables, followed by private variables
#   Avoid public variables
#   After that comes the functions, in an order following the stepdown rule

#   Strongly prefer maximising encapsulation - place tests in the same scope instead of loosening protections for testing purposes

#   Class names should be nouns or noun-phrases
#   Method names should be verb or verb-phrases

#   Classes should be small. They should be smaller than that.
#   The size of a class is measured by counting its responsibilities
#   (contention: a program with more classes is probably better organised than a program with fewer classes that does the same thing)

#   The name of a class should describe what responsibilities it fulfills
#   If there is no concise name that describes those responsibilities, the class is probably too large
#   (contention: the responsibilities of a class should be describable in ~25 words without using the words if/and/or/but)


#   Key OOP concepts:
#       - Abstraction
#       - Encapsulation
#       - Inheritance
#       - Polymorphism
#
#   Abstraction:
#   Presenting a simple interface for a complicated process 
#
#   Encapsulation:
#   Hiding implementation details from the user
#
#   Inheritance:
#   Deriving child classes from parent classes
#
#   Polymorphism:
#   Accessing multiple types through the same interface, objects which pass multiple 'is-a' tests
#   static polymorphism: function overloading
#   dynamic polymorphism: virtual functions


#   Cohesion:
#   A class should have a small number of member variables. 
#   In an ideally cohesive class, every method uses every member variable. A set of member variables that are only used by a subset of methods can be indicative that the class should be divided into multiple more cohesive classes.


#   SOLID Principles:
#       - Single Responsibility
#       - Open/Closed
#       - Liskov Substitution
#       - Interface segregation
#       - dependency inversion


#   Single Responsibility Principle:
#   A class should have only one responsibility - there should be only one reason for it to change
#   Ask: what is the responsibility of the class. If the answer includes the word 'and', the class is probably breaking the single responsibility principle
#   Example: a class, `ReportGenerator`, might have two reasons to change - the content of the report needs to be changed, or the format for the report needs to be changed - suggesting its functionality should be split into `ReportContent` and `ReportWriter` classes
#   <>


#   Organising for change:
#   For most software, change is continual. 
#   A class being difficult to modify can be a sign it is violating the single responsibility principle.
#   [{Using abstract classes can isolate components from the effects of change}]
#   <>


#   The Open/Closed Principle:
#   Classes should be open for extension, but closed for modification
#   [{traditionally implemented through inheritance}]
#   The polymorphic open/closed principle specifies the use of interface classes to achieve this goal
#   [{the use of interfaces prevents tight-coupling, which occurs when a derived class depends on the implementation details of the parent class}]
#   An interface class should specify all the methods that are mandatory for the type in question, but no optional classes which might limit the flexibility of the implementation
#   <>


#   Liskov Substitution:
#   Recall: public inheritance models "is-a"
#   [{Functions receiving base objects must also be able to handle any object derived from it}]
#   [{base/derived objects should be useable interchangeably without breaking the program}]
#   [{write test cases to validate derived classes can be used as base classes}]
#   <>


#   Interface Segregation:
#   Clients should not be forced to depend on methods they do not use
#   Interfaces should not be so large that classes that implement them inherit unwanted methods
#   [{no code should depend on methods it does not use}]
#   An interface class my be violating the interface segregation principle if:
#           - the interface is excessively large
#           - implementations contain unimplemented or unneeded methods
#           - implementations require us to pass null/equivalent as arguments
#   Solutions:
#           - split large interfaces into smaller ones (inheritting from multiple interfaces if required)
#           - (see 'adaptor pattern')
#   <>


#   Dependency Inversion:
#   1) High level modules should not depend on low level modules, both should depend on abstractions
#   2) Abstractions should not depend on details, details should depend on abstractions
#   (high/low level refers to level of abstration of the modules in question)
#   [{put another way, high level modules should depend on interfaces, and low level modules should implement those interfaces(?)}]
#   (contention: code that follows the open/closed principle and liskov substitution principle should also follow the dependency inversion principle)
#   <>
#
#   Example: BasicCoffeeMachine/FancyCoffeeMachine
#   {{{
#   We define a seperate interface class for each type of functionality we require, with each implementation class inheriting those interfaces it [{requires/implements}]
class ICoffeeMachine(ABC):
    @abstractmethod
    def brewFilterCoffee(self):
        raise NotImplementedError()

class IEspressoMachine(ABC):
    @abstractmethod
    def brewEspresso(self):
        raise NotImplementedError()

class BasicCoffeeMachine(ICoffeeMachine):
    def brewFilterCoffee(self):
        return "Basic drip coffee"

class FancyCoffeeMachine(ICoffeeMachine, IEspressoMachine):
    def brewFilterCoffee(self):
        return "Fancy drip coffee"
    def brewEspresso(self):
        return "Fancy espresso coffee"

def test_Coffee_Example():
    b = BasicCoffeeMachine()
    f = FancyCoffeeMachine()
    assert b.brewFilterCoffee() == "Basic drip coffee"
    assert f.brewFilterCoffee() == "Fancy drip coffee"
    assert f.brewEspresso() == "Fancy espresso coffee"
#   }}}
test_Coffee_Example()



#   Interface (abstract) classes:
#   <>


#   Adaptor pattern:
#   <>


#   The visitor pattern:
#   <>


#   The command pattern:
#   <>


#   Fluent interfaces:
#   <>


#   Summary:
#   <>

