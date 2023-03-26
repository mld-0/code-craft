#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import unittest
#   Ongoings:
#   {{{ 
#   Ongoing: 2023-03-26T19:27:33AEDT is factory functions for custom exceptions even a thing in python?
#   }}}

#   5.1) A template for implementing methods
class Foo:
    def methodName(self, arg):
        """"""
        #   precondition checks
        #   failure scenarios
        #   happy path
        #   postcondition checks
        #   return value

#   precondition checks:
#   Ensure arguments provided by client are correct, raise an exception if they are not
#   Arguments can be validated by creating a class for them to handle said validation (especially if validation is otherwise being repeated in multiple places)
#   <>
#
#   failure scenarios:
#   Errors that might occur during the method after precondition checks
#   Use a different sort of exception to precondition checks
#   <>
#
#   happy path:
#   Perform task of method where nothing is wrong
#
#   postcondition checks
#   Verify method did what it was supposed to do
#   (often unnecessary)
#   Consider eliminating by creating new types or moving to another method
#
#   return value
#   Only query methods should return a value.
#   Return early: return the result as soon as it is ready (even if this means creating multiple return points), don't skip over any remaining if-clauses first



#   5.2) Some rules for exceptions
#
#   Use custom exception classes only if needed
#   <>
#
#   A custom exception does not need to contain the word 'exception'
#   Use the word 'Invalid' to indicate invalid arguments, eg: InvalidEmailAddress, InvalidTargetPosition
#
#   A runtime exception name should finish the sentence "sorry, I ..."
#   eg: CouldNotFindProduct, CoundNotConnect
#
#   Use named ctors to indicate reasons for failure
#   <(define (multiple) factory functions for each exception)>
#
#   Add detailed messages
#   The exception ctor should provide the exception message, with only any necessary details being passed as arguments by the client


#   Summary:
#   A method should check preconditions, handle failure scenarios, perform its task (happy path), cehck any postconditions, and return the result
#   Define custom exceptions only if really needed. These should provide useful error messages.

