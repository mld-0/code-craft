#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
from abc import ABC, abstractmethod
#   Ongoings:
#   {{{
#   2023-09-08T21:31:26AEST "the best solution (to the problem of ensuring there is only one instance of a particular class) is to have the class be responsible for keeping track of its sole instance" - is this (another) Pattern where that is true unless the language in question provides a better option?
#   2023-09-08T21:33:06AEST static object ... *doesn't* mean only instance? (a static object is one that exists from the start of the program to the end?)
#   2023-09-08T21:35:42AEST subclassing a Singleton ... one instance of both or either the parent/subclasses? [...] (also, clarify: 'and clients should be able to use an extended instance without modifying their code')
#   2023-09-08T21:39:16AEST when a singleton is created?
#   2023-09-08T21:42:13AEST (see Consequences #3) - are they saying we can configure the application to use a different subclass instead as the only Singleton (or that we can add the subclass as another Singleton?)
#   2023-09-08T21:46:00AEST examples for subclassing / multiple instances?
#   2023-09-08T21:52:14AEST metaclasses(?)
#   }}}

#   Pattern: Singleton

#   Intent:
#   Ensure a class has only one instance, and provide a global point of access to it

#   [{Also known as}]:
#   <>

#   Motivation:
#   It is important for some classes to have exactly one instance.
#   The best solution is to make the class responsible for keeping track of its sole instance (allowing it to intercept requests to create new objects and ensure no other instance is created).

#   Use the Singleton pattern when:
#       -   There must be exactly one instance of a class, and it must be accessible to the client from a well known point
#       -   [{When the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code}]


#   Structure:
class Singleton:
    """"""
    #   <>


#   [{subclassing example?}]
#   <>


#   [{Collaborations}]
#   Clients access a Singleton instance solely through Singleton's instance operation


#   Consequences:
#
#   1)  Controlled access to a sole instance
#   Singleton allows strict control over how/when clients access said single instance
#
#   2)  Reduced namespace
#   Avoids the need to pollute the global namespace with variables to store sole instances
#
#   3)  Permits refinement of operations and representation
#   The Singleton class may be subclassed, [{and we can easily configure the application to use the class we need (at compile/run-time)}]
#
#   4)  Permits a variable number of instances
#   [{The Singleton class can be modified to allow a specific (more than 1) number of instances (only operations that grant access to the Singleton instance need to change)}]
#
#   5)  More flexible than class operations
#   The Singleton pattern is more flexible than using class operations <?> to limit a class to one instance


#   Implementation:
#   
#   1)  Ensure a unique instance
#   The class is written so that one one instance can ever be created. 
#   [{using language (what) language features? (why haven't you written the 'Structure' example yet?)}]
#   <>
#
#   2)  Subclassing the Singleton class
#   <>
#   [{a registry of Singletons}]
#   <>


#   Example: MazeFactory instance
#   <>


#   Related Patterns:
#   Patterns that can be implemented using the Singleton pattern include: Abstract Factory, Builder, and Prototype

