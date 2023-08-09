#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2

#   Ongoing:
#   {{{
#   2023-08-09T16:02:43AEST functions should follow the stepdown rule -> implying we shouldn't put all public functions before all private ones(?)
#   2023-08-09T16:05:51AEST guidelines for putting utility private methods in a utility/helper class instead of cluttering the class - when/whether we consider private methods to be adding the size of a class (which we have defined as a count of its responsibilities)
#   2023-08-09T16:33:50AEST lessons from the `Sql` class before/after case study ... how the `Where` / `ColumnsList` class fall into implementation ... how to reconcile use of inheritance with the ((strongly) prefer composition over inheritance) principle? [...] (the Open/Closed principle implies the use of inheritance?)
#   2023-08-09T17:26:47AEST interface classes and private methods, interface classes and providing <default/mandatory> implementations
#   2023-08-09T17:34:12AEST Liskov Substitution principle - governs design of base/derived classes, design of functions receiving base/derived objects (or both)
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
#   <>


#   Dependency Inversion:
#   <>


#   The visitor pattern:
#   <>

