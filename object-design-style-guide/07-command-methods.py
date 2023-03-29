#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import unittest
from dataclasses import dataclass
#   Notes:
#   {{{
#   2023-03-29T21:24:12AEDT in ch06 it was 'define an abstraction', in ch07 it is 'define abstractions'(?)
#   2023-03-29T21:42:25AEDT alternative solutions to 'changePasswordAndSendEmail()' without event dispatching
#   2023-03-29T21:50:42AEDT a better solution to the 'Emailer' "don't send duplicates" problem ... (define a 'UniqueEmailRecipient' class which does not allow instances to be created with addresses used before) ... (or just don't - if the client attempts to send multiple emails, multiple emails get sent?)
#   }}}

#   7.1) Use command methods with a name in the imperative (commanding) form
#   Query methods have a specific return type and no side effects.
#   Command methods should not return anything, and should have a name which describes the task they perform
#
#   eg: 'sendReminderEmail()', 'saveRecord()'


#   7.2) Limit the scope of a command method, and use events to perform secondary tasks
#   Command methods shouldn't attempt to do too many things. They may be too large if:
#           A descriptive method name includes 'and'
#           It has lines which do not contribute to the task stated in the name

#   (recall: functions should be short, and they should be shorter than that. They should not mix levels of abstraction: if the body of an if-statement or a loop contains more than one line, maybe those lines should be their own function)

#   A method which changes a user's password and sends them an email is doing more than one thing
#   Instead, have the method create a 'PasswordChanged' event object, which it dispatches to a listener that is responsible for sending the email and any other tasks that should be performed after a password is changed.
#   This allows extra tasks to be added without changing the original function, removes any classes involved in sending emails as dependencies from the method, and can be performed from a background thread
#   Dispatching events adds a level of complexity to the application

#   Event dispatching/listener:
#   {{{
#   }}}


#   7.3) Make services immutable from the outside as well as on the inside
#   Service objects should have the same behaviour whether they are newly created or re-used. Command methods on service objects should not have side effects - the behaviour of the service object should not change depending on what methods have previously been called.
#
#   It is not an 'Emailer' service object's job to prevent the client sending duplicate emails
#   (a suggested solution to this problem is defining a Recipients class to which only new addresses can be added)


#   7.4) Throw an exception when something goes wrong
#   Use exceptions, not null/None return values, to indicate an error

#   Use a RuntimeException for errors that can only be established at runtime
#   (eg: id already exists in database)


#   7.5) Use queries to collect information and commands to take the next steps
#   There is no restriction on command methods calling query methods as there is on the reverse.
#   Always consider if the details of a command method could be abstracted further


#   7.6) Define abstractions for commands that cross boundaries
#   <(what is to be said that isn't just a duplicate of 6.5?)>


#   7.7) Only verify calls to command methods with a mock


#   Summary:

