#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   Ongoing: 2022-12-11T22:32:06AEDT ctors and exceptions ('prevent an object being fully instantiated by throwing an exception in the ctor') [...] (also dtors and exceptions)
#   }}}

#   The runtime behaviour of an object is defined by its class definition

#   'Object methods' can only be called on an instance of the class.
#   'Static methods' are called on the class name

#   A constructor is a method which is called to create an object instance
#   A destructor is a method which is called when an object is destroyed

#   A static method that returns an instance of the class is a 'factory function'

#   An object's 'state' is stored in its properties.
#   Properties are object variables. Each will have a name/type.

#   private should be the default scope

#   A mutable object's properties can change during its lifetime

#   An objects behaviour is defined by its methods

#   A class's dependencies are those classes which it requires to function
#   (They may be member variables, or the class may inherit from them)

#   A parent class is oftern known as an 'interface'
#   An abstract class is a class which does not provide an implementation for at least one method

#   <(Subclasses <can/should> only override protected/parent parent class methods)>

#   <(public inheritence models 'is-a')>

#   Polymorphism is where a parent class reference is used to access a child class object
#   (child classes can <provide/define> their own custom behaviour)

#   Composition is where one object contains another (as a member variable) - using it in its implementation
#   <(composition models 'has-a')>


#   (blah blah blah...)

#   Summary:
#   Objects can be instantiated based on a given class.
#   A class defines properties, constants, and methods.
#   Private properties and methods are accessible to instances of the same class. Public properties and methods are accessible to any client of an object.
#   An object is immutable if all of its properties can't be modified, and if all objects contained in those properties are immutable themselves.
#   Dependencies can be created on the fly, fetched from a known location, or injected as constructor arguments (which is called dependency injection).
#   Using inheritance you can override the implementation of certain methods of a parent class. An interface can declare methods but leave their implementations entirely to a class that implements the interface.
#   Polymorphism means that code can use another object's methods as defined by its type (usually an interface), but that the runtime behavior can be different depending on the specific instance that is provided by the client.
#   When an object assigns other objects to its properties, it's called composition.
#   Unit tests specify and verify the behaviors of an object.
#   While testing, you may replace an object's actual dependencies with stand-ins known as test doubles (such as stubs and mocks).
#   Dynamic arrays can be used to define lists or maps without specifying types for its keys and values.

