#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   2023-08-27T22:44:21AEST meaning of 'Product' in this context ... (an object representing something (from the solution space)?)
#   2023-09-01T20:40:07AEST how well does mypy support AbstractFactory like design patterns (passing a `ConcreteFactory1` where an `AbstractFactor` is called for (where ConcreteFactory1 is-an AbstractFactory)) [...] mypy doesn't appear to support argument types (only return types)? [...] but it does permit us to return `ProductB2` where the return type hint is `AbstractProductB` [...] problem is because mypy doesn't check untyped functions by default, unless '--check-untyped-defs' is provided
#   2023-09-01T21:05:24AEST whether ConcreteFactory1.CreateProductA() should have the type hint `AbstractProductA` or `ProductA1` ... (gpt4 says there are arguments for both?)
#   2023-09-01T21:10:40AEST what our `ConcreteFactory1` example doesn't do is take it out of the clients hands whether they get ProductA1/ProductA2? (which is what was described in the problem statement?) [...] (though they would be able to depend on AbstractFactory/AbstractProductA instead of ConcreteFactory/ProductA (which is a different problem?)) [...] (is there another design pattern which encapsulates which type is created for the client?)
#   }}}

#   Pattern: Abstract Factory

#   Intent:
#   Provides an interface for creating families of related or dependent objects without specifying their concrete classes

#   Also known as: 
#           - Kit

#   Motivation:
#   [{prevent clients relying on specific concrete classes, allow flexibility in application behaviour}]
#   <>

#   Use the Abstract Factory pattern when:
#       - A system should be independent of how its products are created, composed, and represented
#       - A system should be configured with one of multiple families of products
#       - [{We need to enforce constraints on how a family of related product objects are used together}]
#       - Creating a library of products which reveal only their interfaces (not their implementations)


#   Structure:
#   {{{
class AbstractProductA:
    ...
class ProductA1(AbstractProductA):
    ...
class ProductA2(AbstractProductA):
    ...

class AbstractProductB:
    ...
class ProductB1(AbstractProductB):
    ...
class ProductB2(AbstractProductB):
    ...

class AbstractFactory:
    def CreateProductA(self) -> AbstractProductA:
        raise NotImplementedError()
    def CreateProductB(self) -> AbstractProductB:
        raise NotImplementedError()

class ConcreteFactory1(AbstractFactory):
    def CreateProductA(self) -> ProductA1:
        return ProductA1()
    def CreateProductB(self) -> ProductB1:
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def CreateProductA(self) -> ProductA2:
        return ProductA2()
    def CreateProductB(self) -> ProductB2:
        return ProductB2()

def recieve_ProductA(p: AbstractProductA) -> None:
    print(p)

def recieve_ProductB(p: AbstractProductB) -> None:
    print(p)

recieve_ProductA(ConcreteFactory1().CreateProductA())
recieve_ProductA(ConcreteFactory2().CreateProductA())
recieve_ProductB(ConcreteFactory1().CreateProductB())
recieve_ProductB(ConcreteFactory2().CreateProductB())
#   }}}


#   [{Collaborations}]
#   Normally, a single instance of ConcreteFactory is created at runtime
#   [{The client choses which ConcreteFactory depending on the behaviour they are after}]
#   [{The client should design their interfaces in terms of AbstractFactory/AbstractProduct}]


#   Consequences:
#
#   1)  Isolates concrete classes 
#   Clients should write their interfaces in terms of AbstractProduct types, not the concrete implementation classes.
#
#   2)  Makes exchanging product families easy 
#   Changing from ProductA1 to ProductA2 should be a matter of simply changing from ConcreteFactory1 to ConcreteFactory2 - [{and there should only be one instance of it to be changed}].
#
#   3)  Promotes consistency among products
#   Declaring only a single ConcreteFactory makes it easier for the client to ensure they use only ProductA1/ProductB1 or ProductA2/ProductB2, and not accidently a mix of the two
#
#   4)  Adding new types of products is difficult
#   Adding a new type, eg: ProductC1/ProductC2, requires modifying both the abstract and concrete factory classes


#   Implementation:
#   
#   1)  Factories as singletons
#   Typically there is only one instance of a ConcreteFactory per product family
#   Therefore it's usually best implemented as a Singleton
#   
#   2)  Creating the products
#   Most commonly, each Product class will define a Factory Method, which is responsible for its creation. This way, the concrete factories only need to specify which Factory Method to call.
#   Where there is many product families, the Prototype pattern can be used for the concrete factories (instead of defining a Factory Method) for each
#   <>
#
#   3)  Defining extensible factories
#   Normally, the AbstractFactory will define a method for each type of object that is to be created
#   A less safe alternative is to define a single method, and pass a parameter to specify the type of object it should create (this can present significant problems in statically typed languages)
#   <>


#   Example: MazeFactory
#   <>


#   Related Patterns:
#   Usually implemented with Factory Methods, but can also use Prototype
#   A concrete factory is oftern a Singleton

