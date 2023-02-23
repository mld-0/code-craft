#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   Ongoing: 2023-02-23T22:50:26AEDT Game of Life, (talk source for before/after) (that 'After' 'advance()' function is so much more horrible than class version (did we see all of class version?)) [...] (apply "we don't need a dict, just use a set" optimisation to class version?)
#   }}}
import functools
import itertools

#   Continue: 2023-02-23T22:55:56AEDT simplified Game of Life (Before) version

#   LINK: https://www.youtube.com/watch?v=o9pEzgHorH0

#   The Zen of Python: (prefer easy things)
#           Simple is better than complex
#           Flat is better than nested
#           Readability counts
#           If the implementation is hard to explain, it's a bad idea
#           If the implementation is easy to explain, it may be a good idea


#   Obfuscated Function Call - A class that is not a class
#   (hint this should not be a class: it has 2 methods, one of which is 'init')
class Greeting:
    def __init__(self, greeting='hello'):
        self.greeting = greeting
    def greet(self, name):
        return '%s! %s' % (self.greeting, name)
greeting = Greeting('hola')
print(greeting.greet('bob'))

#   Fixed:
def greet(greeting, name):
    return '%s! %s' % (greeting, name)
print(greet('hola', 'bob'))

#   Use 'functools.partial' where we pass the same 1st argument repeatedly
greet_hola = functools.partial(greet, 'hola')
print(greet_hola('bob'))
print()


#   I might need this later = implement it later

#   Namespaces are not for creating taxonomies

#   Standard library exceptions are usually enough

#   Containers (combining instructions/data) are a good use case for classes


#   Example: Game of Life 
#
#   (Before)
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def neighbours(self):
        yield (self.x + 1, self.y)
        yield (self.x - 1, self.y)
        yield (self.x, self.y + 1)
        yield (self.x, self.y - 1)
        yield (self.x + 1, self.y + 1)
        yield (self.x + 1, self.y - 1)
        yield (self.x - 1, self.y + 1)
        yield (self.x - 1, self.y - 1)
class Board:
    def __init__(self, glider):
        self.cells = set( [ point for point in glider ] )
    def advance(self):
        newstate = set()
        recalc = self.cells | set(itertools.chain(*[ Cell(*point).neighbours() for point in self.cells]))
        for point in recalc:
            count = sum( (n in self.cells) for n in Cell(*point).neighbours() )
            if count == 3 or (count == 2 and point in self.cells):
                newstate.add(point)
        self.cells = newstate
board = Board([ (0,0), (1,0), (2,0), (0,1), (1,2), ])
for i in range(10):
    board.advance()
print(board.cells)
#
#   (After)
def neighbours(point):
    x, y = point
    yield (x + 1, y)
    yield (x - 1, y)
    yield (x, y + 1)
    yield (x, y - 1)
    yield (x + 1, y + 1)
    yield (x + 1, y - 1)
    yield (x - 1, y + 1)
    yield (x - 1, y - 1)
def advance(board):
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbours, board)))
    for point in recalc:
        count = sum( (n in board) for n in neighbours(point) )
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)
    return newstate
glider = set( [ (0,0), (1,0), (2,0), (0,1), (1,2), ] )
for i in range(10):
    glider = advance(glider)
print(glider)

