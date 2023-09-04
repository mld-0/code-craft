#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   2023-09-04T21:31:48AEST should we have a DefaultProduct (something for `Creator` to return?)
#   2023-09-04T21:54:39AEST further elaborate on how Factory Method and Abstract Factory are different and alike
#   }}}

#   Pattern: Factory Method

#   Intent:
#   Define an interface for creating an object, but defer subclass

#   Also known as:
#       -   Virtual Constructor

#   Motivation:
#   <>


#   Use the Factory Method pattern when:
#       -   A class can't anticipate the type of object it must create
#       -   A class wants its subclasses to specify the object it creates
#       -   [{to localize which helper subclass a parent class is delegating to}]


#   Structure:
class Product:
    """Defines the interface of ConcreteProduct objects"""
    def operation(self) -> str:
        raise NotImplementedError()

class ConcreteProductA(Product):
    """Implements the Product interface"""
    def operation(self) -> str:
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"

class Creator:
    """ Declares the factory method (and may also provide a default implementation)
        [{may call the factory method to create a Product object}]"""
    def make_Product(self) -> Product:
        raise NotImplementedError()

class ConcreteCreatorA(Creator):
    """Overrides Creators default factory method to return [{different?}] ConcreteProducts"""
    def make_Product(self) -> ConcreteProductA:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def make_Product(self) -> ConcreteProductB:
        return ConcreteProductB()

def client():
    def recieve_Product(p: Product):
        print(p.operation())
    creator = ConcreteCreatorA()
    recieve_Product(creator.make_Product())
    creator = ConcreteCreatorB()
    recieve_Product(creator.make_Product())

client()


#   [{Collaborations}]
#   [{Creator relies on its subclasses to define the factory method to return an instance of the appropriate ConcreteProduct}]


#   Consequences:
#   [{Eliminates the need to bind application-specific classes into code}]
#   [{(has the disadvantage that) clients might have to subclass Creator in order to create a particular (new?) ConcreteProduct?}]
#   <>
#
#   1)  Provides a hook for subclasses
#   [{Creating objects with Factory Methods is more flexible than creating the object directly}]
#   <>
#   
#   2)  Connects parallel class hierarchies
#   <>


#   Implementation:
#   
#   1)  Two major variants
#   Creator may or may-not provide a default implementation for the factory method it declares
#   [{Not providing a default implementation makes sense when there is no reasonable default}]
#
#   2)  Parameterised factory methods:
#   An alternative, where each factory method takes a parameter, and may return a range of different ConcreteProduct objects accordingly (each sharing the same interface from Product)
#   <>
#   
#   3)  Language-specific variants and issues:
#   <>
#   
#   4)  Use templates to avoid subclassing
#   [{We can avoid having to create various subclasses by creating a single template class and returning different instantiations of it}]
#   <>
#
#   5)  Naming conventions:
#   <>


#   Example: CreateMaze
#   <>


#   Related Patterns:
#   Abstract Factory is often implemented by Factory Methods
#   [{Template Methods usually call Factory Methods}]
#   [{Prototypes don't require subclassing Creator, however (unlike Factory Methods) they do often require an initalize operation on the Product class}]

