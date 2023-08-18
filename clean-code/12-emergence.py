#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import sys
import os
import tempfile

#   Four rules for a simple design:
#       1)  Runs all tests
#       2)  Contains no duplication
#       3)  Expresses the intent of the programmer
#       4)  Minimises number of classes and methods


#   Runs all tests:
#   Tests verify that a system actually behaves the way it is designed
#   Contention: deviating from the single-responsibility-principle complicates testing, and writing tests leads to better design
#   Having tests greatly simplifies the process of refactoring code


#   Contains no duplication:
#   Contention: duplication is the enemy of a well-designed system.
#   [{Begin by extracting duplication between methods into new methods. From these sort of small changes, it may become more evident where the single-responsibility-principle is violated, and functionality should be extracted into new classes}]


#   Template method pattern:
#   (A technique for removing higher-level duplication)
#   Define a superclass for the algorithm we wish to represent
#   The template method is the method that defines the algorithm as a series of steps, each provided by a helper method. 
#   Helper methods may be implemented, or left as abstract to be provided by subclasses as appropriate
#
#   Example: `TableReader` class 
#   {{{
#   Interface class:
class TableReaderInterface():
    def read(self, path):
        f = self.openFile(path)
        buffer = self.readFile(f)
        raw_table = self.extractTable(buffer)
        table = self.parseTable(raw_table)
        return table 
    def openFile(self, path):
        raise NotImplementedError()
    def readFile(self, f):
        raise NotImplementedError()
    def extractTable(self, buffer):
        raise NotImplementedError()
    def parseTable(self, data):
        def parse_cell(cell):
            try:
                return float(cell)
            except ValueError:
                return cell
        return [ [ parse_cell(cell) for cell in row ] for row in data ]

#   Implementation:
class CSVReader(TableReaderInterface):
    def openFile(self, path):
        return open(path, 'rt')
    def readFile(self, f):
        return f.read()
    def extractTable(self, buffer):
        row_delim = ','
        line_delim = '\n'
        return [ l.split(row_delim) for l in buffer.split(line_delim) if len(l) > 0 ]

def test_CSVReader():
    #   {{{
    expected_data = [
        ['Name', 'Age', 'Occupation', 'Salary'],
        ['Alice', 30.0, 'Engineer', 75000.5],
        ['Bob', 35.0, 'Doctor', 100000.0],
        ['Charlie', 40.0, 'Teacher', 65000.0]
    ]
    test_file_path = None
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        for d in expected_data:
            f.write(','.join([ str(x) for x in d ]) + '\n') 
        test_file_path = f.name
    reader = CSVReader()
    data = reader.read(test_file_path)
    os.remove(test_file_path)
    assert data == expected_data
    #   }}}
test_CSVReader()
#   }}}


#   Expressive:
#   Make a deliberate effort to write code that is as self-documenting as possible.
#   Choose good names. Keep functions and classes small. 
#   Use design-pattern names (eg: 'Command', 'Visitor') in the names of classes that use those patterns.
#   Well written tests act as documentation-by-example


#   Minimal classes and methods:
#   Don't bloat the overall size of the project by taking code-craft principles too far. 
#   There is a balance between keeping methods/classes small, and allowing the number of them to explode.


#   Summary:
#   <>

