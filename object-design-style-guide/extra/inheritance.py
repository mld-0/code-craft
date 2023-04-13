#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Notes:
#   {{{
#   2023-04-05T19:35:00AEST instead of printing A B C - capture output and assert it against expected value
#   2023-04-05T19:35:28AEST behaviour of all examples same for different python versions?
#   2023-04-13T21:01:19AEST traits -> see effective-rust(?)
#   }}}

#   calling 'super()'
#   Calls to base class ctors can be made as 'A.__init__(self)' or 'super().__init__()'
#   (the former does not allow for dependency injection; use 'super()' instead)
#   (use 'A.foo()' instead of 'super()' to explicitly access methods of 'A')



#   Python handles multiple-inheritance badly

#   'super()' is equivalent to 'super(type(self), self)'

#   'super(Foo, self).method()'
#   call next 'method()' in the method resolution order that comes after class 'Foo'

#   multiple inheritance with unrelated base classes:
#   If C does not declare a constructor, then the constructor of A but not the constructor of B is called
#   If C declares a constructor, the constructors of A/B must be called manually
def _multi_inheritance_1():
    class A:
        def __init__(self):
            print("A, ", end="")
    class B:
        def __init__(self):
            print("B, ", end="")

    #   correct: 'A B C1'
    class C1(A, B):
        def __init__(self):
            super().__init__()              #   calls A.__init__()  (equivalent to 'super(C1, self)')
            super(A, self).__init__()       #   calls B.__init__()
            print("C1, ", end="")

    #   incorrect: 'B C2'
    class C3(A, B):
        def __init__(self):
            super(A, self).__init__()       #   calls B.__init__()
            super(B, self).__init__()       #   calls nothing
            print("C3, ", end="")

    #   incorrect: 'A C4'
    class C4(A, B):
        def __init__(self):
            super().__init__()
            print("C4, ", end="")

    c = C1(); print();
    c = C3(); print();
    c = C4(); print();
    print()
_multi_inheritance_1()


#   multiple inheritance when all classes in hierachy call 'super().__init__()'
#   <(Classes whose base class is 'Object' should not call super().__init__() ... (shouldn't, or don't need to?))>
def _multi_inheritance_2():
    class A:
        def __init__(self):
            super().__init__()
            print("A, ", end="")
    class B:
        def __init__(self):
            super().__init__()
            print("B, ", end="")

    #   correct: 'B A C'
    class C1(A, B):
        def __init__(self):
            super().__init__()
            print("C, ", end="")

    #   correct: 'A B C'
    class C2(B, A):
        def __init__(self):
            super().__init__()
            print("C, ", end="")

    c = C1(); print();
    c = C2(); print()
    print()
_multi_inheritance_2()


#   (placing argument var before args/kwargs allows arguments to be made as either positional or named values - place these vars between args/kwargs to require them to be given as named arguments)
def _multi_inheritance_handling_args():
    class A:
        def __init__(self, a):
            print(f"A({a}), ", end="")
    class B(A):
        def __init__(self, b, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"B({b}), ", end="")
    class C(A):
        def __init__(self, c, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"C({c}), ", end="")
    class D(B, C):
        def __init__(self, d, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"D({d}), ", end="")

    d = D(1, 2, 3, 4); print()
    d = D(a=4, b=3, c=2, d=1); print()
    print()
_multi_inheritance_handling_args()



#   interface (abstract) base classes
#   (interface classes without inheritance?)


#   traits vs interface classes
#   <(Traits are a form of code reuse that are like but distinct from tradition inheritence)>
#   Traits allow default implementations <(interface classes often do not?)>
#   <(traits do not modify the class hierachy - presumedly refering to langauge other than python)>
#   Traits are often used to encapsulate common behaviour for reuse - logging, error handling, or serializaiton

def _printable_trait():

    class Printable:
        def print(self):
            print(self)
    class Person(Printable):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __repr__(self):
            return f"{self.name}, {self.age}"

    person = Person("John Doe", 30)
    person.print()

_printable_trait()


#   mixins are like traits, but typically rely on composition instead of inheritance
def _printable_mixin():

    class PrintableMixin:
        def print(self):
            print(self)

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __repr__(self):
            return f"{self.name}, {self.age}"

    class PrintablePerson(PrintableMixin):
        def __init__(self, person):
            self.person = person
        def __repr__(self):
            return repr(self.person)

    person = Person("John Doe", 30)
    printable_person = PrintablePerson(person)
    printable_person.print() 

_printable_mixin()


#   final classes


#   public/protected/private inheritance

