#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import sys
import io
import difflib
from contextlib import redirect_stdout
#   Notes:
#   {{{
#   2023-04-05T19:35:00AEST instead of printing A B C - capture output and assert it against expected value
#   2023-04-05T19:35:28AEST behaviour of all examples same for different python versions?
#   2023-04-13T21:01:19AEST traits -> see effective-rust(?)
#   2023-04-13T22:40:36AEST 'check_stdout()' is in SnippetsLab (plz update on change)
#   2023-04-13T23:09:48AEST traits and dependency injection
#   }}}

def check_stdout(obj, check, *args, **kwargs):
    """Validate stdout from 'x = obj(*args, **kwargs)' matches 'check' verification"""
    #   {{{
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        x = obj(*args, **kwargs)
    result = buffer.getvalue().strip()
    if not result == check:
        diff = list(difflib.ndiff(result.splitlines(), check.splitlines()))
        print("error, check failed:\n%s" % '\n'.join(diff).rstrip())
        exit(2)
    print(result)
    #   }}}


#   Python handles multiple-inheritance badly

#   calling 'super()'
#   Calls to base class ctors can be made as 'A.__init__(self)' or 'super().__init__()'
#   (the former does not allow for dependency injection; use 'super()' instead)
#   (use 'A.foo()' instead of 'super()' to explicitly access methods of 'A')

#   'super()' 
#           is equivalent to:
#   'super(type(self), self)'

#   'super(Foo, self).method()'
#   call next 'method()' in the method resolution order that comes after class 'Foo'

#   multiple inheritance with unrelated base classes:
#   If C does not declare a constructor, then the constructor of A but not the constructor of B is called
#   If C declares a constructor, the constructors of A/B must be called manually
def _multi_inheritance_1():
    class A:
        def __init__(self):
            print("A", end="|")
    class B:
        def __init__(self):
            print("B", end="|")

    #   correct: 'A|B|C1'
    class C1(A, B):
        def __init__(self):
            super().__init__()              #   calls A.__init__()  (equivalent to 'super(C1, self)')
            super(A, self).__init__()       #   calls B.__init__()
            print("C1", end="")

    #   incorrect: 'B|C3'
    class C3(A, B):
        def __init__(self):
            super(A, self).__init__()       #   calls B.__init__()
            super(B, self).__init__()       #   calls nothing
            print("C3", end="")

    #   incorrect: 'A|C4'
    class C4(A, B):
        def __init__(self):
            super().__init__()              #   calls only first base class ctor
            print("C4", end="")

    check_stdout(C1, "A|B|C1")
    check_stdout(C3, "B|C3")
    check_stdout(C4, "A|C4")
    print()

_multi_inheritance_1()


#   multiple inheritance when all classes in hierachy call 'super().__init__()'
#   <(Classes whose base class is 'Object' should not call super().__init__() ... (shouldn't, or don't need to?))>
def _multi_inheritance_2():
    class A:
        def __init__(self):
            super().__init__()
            print("A", end="|")
    class B:
        def __init__(self):
            super().__init__()
            print("B", end="|")

    #   correct: 'B|A|C1'
    class C1(A, B):
        def __init__(self):
            super().__init__()
            print("C1", end="")

    #   correct: 'A|B|C2'
    class C2(B, A):
        def __init__(self):
            super().__init__()
            print("C2", end="")

    check_stdout(C1, "B|A|C1")
    check_stdout(C2, "A|B|C2")
    print()

_multi_inheritance_2()


#   (placing argument var before args/kwargs allows arguments to be made as either positional or named values - place these vars between args/kwargs to require them to be given as named arguments)
def _multi_inheritance_handling_args():
    class A:
        def __init__(self, a):
            print(f"A({a})", end="|")
    class B(A):
        def __init__(self, b, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"B({b})", end="|")
    class C(A):
        def __init__(self, c, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"C({c})", end="|")
    class D1(B, C):
        def __init__(self, d, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"D1({d})", end="")
    class D2(C, B):
        def __init__(self, d, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"D2({d})", end="")

    check_stdout(D1, "A(4)|C(3)|B(2)|D1(1)", 1, 2, 3, 4)             #   D1(1, 2, 3, 4)
    check_stdout(D2, "A(4)|B(3)|C(2)|D2(1)", 1, 2, 3, 4)             #   D2(1, 2, 3, 4)
    check_stdout(D1, "A(4)|C(2)|B(3)|D1(1)", a=4, b=3, c=2, d=1)     #   D1(a=4, b=3, c=2, d=1)
    check_stdout(D2, "A(4)|B(3)|C(2)|D2(1)", a=4, b=3, c=2, d=1)     #   D2(a=4, b=3, c=2, d=1)
    print()

_multi_inheritance_handling_args()



#   interface (abstract) base classes
#   (interface classes without inheritance?)


#   traits vs interface classes
#   <(Traits are a form of code reuse that are like but distinct from tradition inheritence)>
#   Traits allow default implementations <(interface classes often do not?)>
#   <(traits do not modify the class hierachy - presumedly refering to langauge other than python)>
#   Traits are often used to encapsulate common behaviour for reuse - logging, error handling, or serializaiton
#   <>

def _printable_trait():

    class Printable:
        def print(self):
            print(self)
    class Person(Printable):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __repr__(self):
            return f"I am {self.name}, age {self.age}"

    person = Person("John Doe", 30)
    check_stdout(person.print, "I am John Doe, age 30")

_printable_trait()


#   mixins are like traits, but typically rely on composition instead of inheritance
#   <>

def _printable_mixin():

    class PrintableMixin:
        def print(self):
            print(self)

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __repr__(self):
            return f"I am {self.name}, age {self.age}"

    class PrintablePerson(PrintableMixin):
        def __init__(self, person):
            self.person = person
        def __repr__(self):
            return repr(self.person)

    person = Person("John Doe", 30)
    printable_person = PrintablePerson(person)
    check_stdout(printable_person.print, "I am John Doe, age 30z")

_printable_mixin()


#   final classes


#   public/protected/private inheritance

