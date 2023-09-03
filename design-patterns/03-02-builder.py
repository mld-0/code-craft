#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from typing import List, Optional
#   Ongoings:
#   {{{
#   2023-09-02T19:51:58AEST meaning of 'representation of an object'
#   2023-09-03T20:18:24AEST if `Product` 'represents' the object under construction - does that mean what we are ultimately returning is a type other than `Product`?
#   2023-09-03T20:35:12AEST 'letting clients override only operations they're interested in' - what is being left to the client to write (is there an expectation they'll be writing ConcreteBuilders/Products?)
#   2023-09-03T20:40:28AEST (is) combining Builder with Abstract Factory (a thing?)
#   2023-09-03T20:44:57AEST (validating example gpt4 helped write) (it's describing the same thing as MazeBuilder?)
#   2023-09-03T20:57:58AEST working more than one type of `ConcreteBuilder` into our 'structure' example(?)
#   2023-09-03T21:13:46AEST the 'structure' example has only one type of Product class ... because the Builder pattern is more [{concerned-with/about}] multiple ways of creating the same type of object than creating different types of objects
#   }}}

#   Pattern: Builder

#   Intent: [{Separate construction of complex objects from their representation, so that the same construction process can create different representations}]

#   Motivation:
#   [{Build a complex object using simple objects and a step-by-step approach}]
#   <>


#   Use the Builder pattern when:
#       -   The algorithm for creating an object should be independent of the parts that make up the object
#       -   [{The construction process must allow different representations for the object}]


#   Structure:
#   {{{
class Product:
    """ Represents the object under construction
        Includes classes that define the constituent parts, 
        and assembling these parts into the final result"""
    def __init__(self):
        self.title: Optional[str] = None
        self.header: Optional[str] = None
        self.body: Optional[str] = None
        self.footer: Optional[str] = None
    def to_string(self):
        parts = [ self.title, self.header, self.body, self.footer, ]
        result = ""
        for x in parts:
            if x:
                result += x + "\n"
        return result

class Builder:
    """Abstract interface for creating parts of a Product object"""
    def add_title(self, title: str):
        pass
    def add_header(self, header: str):
        pass
    def add_body(self, body: str):
        pass
    def add_footer(self, footer: str):
        pass
    def get_result(self):
        pass

class ConcreteBuilder:
    """ Implements the abstract `Builder` interface
        Defines and tracks the representation it creates
        Provides an interface for retrieving the built object"""
    def __init__(self):
        self.reset()
    def reset(self):
        self.document = Product()
    def add_title(self, title: str):
        self.document.title = title
    def add_header(self, header : str):
        self.document.header = header
    def add_body(self, body: str):
        self.document.body = body
    def add_footer(self, footer: str):
        self.document.footer = footer
    def get_result(self) -> Product:
        result = self.document
        self.reset()
        return result

class Director:
    """Constructs an object using Builder interface"""
    def __init__(self, builder: Builder):
        self.builder = builder
    def construct_simple_example(self):
        self.builder.add_title("Simple Example")
        self.builder.add_body("Body of a Simple Example")
    def construct_complex_example(self):
        self.builder.add_title("Complex Example")
        self.builder.add_header("Complex Header")
        self.builder.add_body("Body of a Complex Example")
        self.builder.add_footer("Complex Footer")

def run_example():
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct_simple_example()
    simple_example = builder.get_result()
    director.construct_complex_example()
    complex_example = builder.get_result()
    print(simple_example.to_string())
    print(complex_example.to_string())
run_example()

#   }}}


#   [{Collaborations}]
#   -   client creates a Director object and configures it with the desired Builder object
#   -   Director notifies Builder when a part of the product should be built
#   -   Builder handles requests from Director and adds parts to the product
#   -   Client retrieves the Product from the Builder


#   Consequences:
#
#   1)  Lets us vary a Product's internal representation
#   <>
#
#   2)  Isolates code for construction and representation
#   Encapsulates the way a complex object is constructed and represented
#   <>
#
#   3)  Gives us finer control over the construction process
#   <>


#   Implementation:
#   
#   1)  Assembly and construction interface
#   Builders construct Products in a step-by-step fashion. The Builder interface must be general enough to allow construction of Products for different kinds of ConcreteBuilders.
#   [{A key design concern is modeling the construction and assembly process}]
#   <>
#
#   2)  No abstract class for Products
#   [{Products produced by ConcreteBuilders differ enough that there is little to gain from having a common parent interface class}]
#   The client is in a position to know which ConcreteBuilder is in use (since the typically configure the Director with a specific ConcreteBuilder)
#   <>
#
#   3)  [{Empty methods as default in Builder}]
#   Build methods are intentionally not declared as abstract methods (but as empty instead), letting clients override only the operations they're interested in.


#   Example: MazeBuilder
#   <>


#   Related Patterns:
#   Abstract Factory is also responsible for construction of complex objects, however Builder focuses on construction step-by-step, while Abstract Factory manages the creation of families of objects. Builder returns the Product as the final step, while Abstract Factory is generally only called as a single step.
#   [{Composite is generally what a Builder creates}]

