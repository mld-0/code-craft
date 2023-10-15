#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   2023-10-15T19:21:25AEDT Adaptee/Adapter are not class names conducive to taking in example(s) at a glance (what order should they be defined in?)
#   2023-10-15T19:25:01AEDT Is the interface class `Target` really necessary for our example?
#   2023-10-15T19:27:14AEDT For Object_Adapter ... doesn't requiring an instance of Adaptee to be passed to the ctor of Adapter defeat the purpose - shouldn't Adapter be responsible for creating the instance of Adaptee?
#   2023-10-15T19:35:48AEDT related patterns - why is 'Proxy' included, what does it actually have to do with Adapter?
#   }}}

#   TODO: 2023-10-15T19:18:39AEDT reconcile gpt4 provided Class_Adapter / Object_Adapter interpretations from diagram with chapter example(?) (lookup notation used in said diagram?) (add notation reference to this folder?)

#   Pattern: Adapter

#   Intent:
#   Convert the interface of a class into another interface the client expects. Allow classes to work together that couldn't otherwise due to incompatible interfaces

#   Also known as:
#           - Wrapper

#   Motivation:
#   [{Change the interface through which the functionality of a class is made available}]
#   <>

#   Use the Adapter pattern when:
#       -   The interface of an existing class does not match the interface needed
#       -   To (re)use a class which doesn't have a compatible interface 
#       -   [{to adapt the interface of the parent class instead of a range of subclasses}]


#   Structure:
def Class_Adapter():
    """A Class Adapter uses multiple-inheritance to adapt one interface to another"""

    class Target:
        """Defines the interface to be used by our wrapper"""
        def request(self):
            pass

    class Adaptee:
        """Existing class to be wrapped"""
        def SpecificRequest(self):
            print("(Class_Adapter) Adaptee->SpecificRequest()")

    class Adapter(Target, Adaptee):
        """Provides a new implementation for the existing class"""
        def request(self):
            self.SpecificRequest()

    def client():
        x = Adapter()
        x.request()

    client()

Class_Adapter()


#   Structure:
def Object_Adapter():
    """An Object Adapter uses composition to adapt one interface to another"""

    class Target:
        """Defines the interface to be used by our wrapper"""
        def request(self):
            pass

    class Adaptee:
        """Existing class to be wrapped"""
        def SpecificRequest(self):
            print("(Object_Adapter) Adaptee->SpecificRequest()")

    class Adapter(Target):
        """Provides a new implementation for the existing class"""
        def __init__(self, adaptee):
            self.adaptee = adaptee
        def request(self):
            self.adaptee.SpecificRequest()

    def client():
        adaptee = Adaptee()
        target = Adapter(adaptee)
        target.request()

    client()

Object_Adapter()


#   Collaborations:
#   Clients call on an Adapter instance to perform operations. Adapter in-turn calls Adaptee to carry out the request


#   Consequences:
#
#   Class Adapter vs Object Adapter:
#   <>
#   
#   Other issues:
#   <>


#   Implementation:
#   <>


#   Example: TextShape adapter
#   <>


#   Related Patterns:
#   Bridge is similar to Object Adapter, but has a different intent: to separate interface from implementation so they can [{both?}] be varied easily and independently.
#   [{Decorator enhances another object without changing its interface - it is more transparent to the application than an adapter (allowing recursive-composition, not possible with Adapter)}]
#   Proxy defines a representative or surrogate for another object, but does not change its interface 

