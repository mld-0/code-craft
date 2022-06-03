#	VIM SETTINGS: {{{3
#	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#	vim: set foldlevel=2 foldcolumn=2:
#	}}}1
import sys
import os
import logging
import typing
import abc
from io import StringIO
#	{{{2
#   Ongoings:
#	{{{
#	Ongoing: 2022-05-20T19:50:22AEST expand/provide-definitions until source is compile-able
#	Ongoing: 2022-05-20T18:56:57AEST C++ makes this (step-down) rule a PITA, requiring functions to be declared before they are used
#	Ongoing: 2022-05-20T18:57:19AEST C++, observing the step-down rule in a language wehre every function must be declared before it is used
#	Ongoing: 2022-05-18T03:08:47AEST a hierachy to functions (namespaces? classes?), beyond simply having function explosion at global scope (how would one do it for book examples?) (see above)
#	Ongoing: 2022-05-20T18:33:18AEST (there must be) a better before/after example than what the book presents?
#	Ongoing: 2022-05-20T18:46:02AEST is 'isTestPage()' (as its own function) really necessary?
#   Ongoing: 2022-05-24T17:56:35AEST Stepdown rule, functions vs methods?
#   Ongoing: 2022-05-30T23:28:25AEST Stepdown rule (example) - really best not to group public methods?
#   Ongoing: 2022-05-30T23:33:03AEST The stepdown rule (when to ignore it?)
#   Ongoing: 2022-05-30T23:41:46AEST is a function too long (rule 1): questions to ask to answer this question(?)
#	}}}
#	TODO: 2022-05-18T02:12:01AEST code-craft/clean-code/03-functions, plausible data-flow / roles for each object, complete example doing something that makes calls of 'renderPageWithSetupsAndTeardowns' make sense
#   TODO: 2022-05-21T06:18:14AEST code-craft/clean-code/03-functions, verification/enforcing of python type hints (primative/custom types)
#	Continue: 2022-05-18T23:48:43AEST example 'renderPageWithSetupsAndTeardowns' is later explored implemented as a class (called 'uncle_bob' in book source)
#   Continue: 2022-05-30T22:56:52AEST how to best handle error-codes</errors> (where one cannot use exceptions)


#	Functions implement subroutines in modern languages. 
#	They are the first line of organization in any program.


#	Rule 1: Small
#	The first rule of functions is that they should be small. (The second rules is they should be even smaller than that. Functions should hardly ever be 20 lines long).
#	Blocks within if/else/for/while statements should be one line long (probably a function call).
#	This adds documentary value, because every block gets a descriptive name.
#	Limit nested structures, ideally not more than 2 levels.

#   Is a function too long:
#           Is it more than 20 names?
#           Is it difficult to decide on a name?
#           <?>


#	Rule 2: Do One Thing
#	Functions should do one thing. They should do it well. They should do it only. If a function does only those steps that are one level below the stated name of the function, then the function is doing only one thing. 
#	The purpouse of a function is to decompose a larger concept (described by the function name) into steps at the next level of abstraction.
#	Or: <(Functions that do one thing cannot be reasonably divided into sections, if one can extract another function with a name that is not merely a restatement of the containing functions implementation, that function is doing more than one thing)> <(if you have a hard time deciding what the name of a method should be, then the method is probably doing too many things)>



#	Rule 3: Single Level of Abstraction per Function
#	Mixing levels of abstraction in the same function is always confusing. It makes unclear what is an essential concept and what is a detail. When essential concepts and details are mixed in a function, more and more details tend to accumulate in that function.
#   
#   Don't make me think - keeping exclusively to a higher level of abstraction means not presenting the reader with statements whose purpose they have to decipher themselves - a function call is self documenting, because the function name should describe what the function does.
def isUserValid(user: 'User') -> bool:
    return isUnique(user) and isValidPassword(user.password) and isValidEmail(user.email) and isAdult(user.dob)
#   
def makeBreakfast():
    cook()
    #   Bad:
    plate_wife.give(fryingPan.getServing(20))
    plate_husband.give(fryingPan.getServing(80))
    #   Fixed:
    serve()
#
#   Example: mixed levels of abstraction
def MarkdownPost_MixedAbstraction(resource: 'Resource'):
    data = parseResource(resource)
    metaData = extractResourceMetaData(parsedResource)
    #   Bad:
    url = "/" + resource.getFileName().replace(EXTENSION, "")
    #   Fixed:
    url = urlForResource(resource)
def urlForResource(resource: 'Resource') -> str:
    return "/" + resource.getFileName().replace(EXTENSION, "")


#	Rule 4: The Stepdown Rule
#	Caller functions should reside above callee functions - code should read like a top-down narrative, higher levels of abstraction above lower ones. (Where a function is used by multiple caller functions, place it below the last caller). Justification: when reading one function, people are more likely to refer-to its callee functions than to other similar functions.
#
#   Example: Grouping similar functions vs grouping 
#       class Bad():
#			public void MakeBreakfast()
#			public void MakeDinner()
#			private void cookBreakfast()
#			private void cookDinner()
#			private void serveBreakfast()
#			private void serveDinner()
#			private void cleanup()
#       class Good():
#			public void MakeBreakfast()
#			private void cookBreakfast()
#			private void serveBreakfast()
#			public void MakeDinner()
#			private void cookDinner()
#			private void serveDinner()
#			private void cleanup()


#	Rule 5: Descriptive names
#   A name should describe what a function does. A function should do what its name implies.
#   Use a naming convention makes multiple word names readable: camelCase / snake_case / <?>
#   A long descriptive name is better than a short enigmatic name, or a descriptive comment.
#   Spend some time chosing a name. Be prepared to replace a name with a better one.
#   Be consistent with naming. Use the same phrases / nouns / verbs for both functions and modules.


#	Rule 6: Have No Side Effects
#	A side effect is when a function relies on, or modifies, something outside its parameters.
#   Functions that have no side effects are easier to test, and easier to parallelize.
#   Side effects are lies - things a function may do that may not be immediately apparent.
#   Results in temporal couplings and order dependencies.
#   Temporal coupling: time related dependency, when something can be run.
#   Where temporal couplings are necessary, it should be apparent in the function name.
#   Ongoing: 2022-05-30T23:15:51AEST Have no side effects (rule 6) and functional programming (is the way to do it?) 

#   Functional Programming: <(and side-effects?)>
#   {{{
#   LINK: https://www.yld.io/blog/the-not-so-scary-guide-to-functional-programming/#:~:text=A%20side%20effect%20is%20when,described%20as%20having%20side%20effects.
#   (Functional programming is about) keeping buisness logic as pure functions and moving side effects to the edges of our process.
#   Referential transparency: a function can be replaced with its result (and vice-versa) without incuring side effects.
#   Replacing loops: map() / filter() / reduce()
#   }}}


#	Rule 7: Command Query Separation
#	A function should do something, or answer something, but not both.
#   Methods should either change the state of an object, or return information about the object, but not both.
#   Bad:
#           if not checkExistsAndSet('username', 'bob'):
#               raise Exception()
#   Better:
#           if attributeExists('username'):
#               setAttribute('username', 'bob')


#	Rule 8: Prefer Exceptions to Error Codes:
#   Returning error codes is a violation of command-query-separation.
#   Exceptions allow error processing code to be separated from logic.
#   Doing so leads to messy deeply nested structures, since the caller must deal with any error immediately.
#   Extract bodies of try-catch block into its own function, allowing complete separation of error handling and logic, and preserving Rule 2: 'Do One Thing'.
#
#   Example: use of error codes vs use of exceptions
def HandleDeletePage_ErrorCodes(path):
    if deletePage(page) == E_OK:
        if registery.deleteReference(page.name) == E_OK:
            if configKeys.deleteKey(page.name.makeKey()):
                logging.debug('done delete')
            else:
                logging.error('failed to delete key')
        else:
            logging.error('failed to delete reference')
    else:
        logging.error('failed to delete page')
#   note that implementation / error-handling are seperate functions (Rule 2)
def HandleDeletePage_Exceptions(path):
    try:
        PerformDeletePage(page)
        logging.debug('done delete')
    except Exception as e:
        logging.error(e)
def PerformDeletePage(path):
    deletePage(page)
    registery.deleteReference(page.name)
    configKeys.deleteKey(page.name.makeKey())


#	Rule 9: Don't Repeat Yourself
#	Duplication is (one of) the root(s) of all evil in software.
#   <(Codd's database normal forms(?))>


#   Rule 10: Switch-like statements
#   There should only be one declaration of such a statement - buried in an AbstractFactory class which returns an appropriate polymorphic objects to handle whatever specific behaviour is required for a given input.
#   <(Must grow as new options are added (violation of Open Closed Principle))>
#   <(More than one reason for it to change(?) (violation of Simple Responsibility Principle))>
#   {{{
class EmployeeRecord:
#   {{{
    def __init__(self):
        self.kind = None
#   }}}
class Employee(abc.ABC):
#   {{{
    @abc.abstractmethod
    def isPayday(self):
        raise NotImplementedError()
    @abc.abstractmethod
    def calculatePay(selfj):
        raise NotImplementedError()
    @abc.abstractmethod
    def delieverPay(self, pay: 'Money'):
        raise NotImplementedError()
#   }}}
class FullTimeEmployee(Employee):
#   {{{
    def isPayday(self):
        return False
    def calculatePay(self):
        return 53
    def delieverPay(self, pay: 'Money'):
        pass
#   }}}
class PartTimeEmployee(Employee):
#   {{{
    def isPayday(self):
        return False
    def calculatePay(self):
        return 27 
    def delieverPay(self, pay: 'Money'):
        pass
#   }}}
class HourlyEmployee(Employee):
#   {{{
    def isPayday(self):
        return False
    def calculatePay(self):
        return 12 
    def delieverPay(self, pay: 'Money'):
        pass
#   }}}
#   }}}
def EmployeeFactory(r: 'EmployeeRecord'):
    if r.kind is FullTimeEmployee:
        return FullTimeEmployee(r)
    elif r.kind is PartTimeEmployee:
        return PartTimeEmployee(r)
    elif r.kind is HourlyEmployee:
        return HourlyEmployee(r)
    else:
        raise Exception("Invalid employee kind=(%s)" % str(r.kind))


#	Rule 10: Function arguments best practices
#   	  0 = niladic         (best)
#         1 = monadic
#         2 = dyadic
#         3 = triadic         (avoid)
#        >3 = polyadic        (strongly avoid)
#   More arguments make a function harder to read, and harder to test.
#   Output arguments should be avoided. Use return to output data instead.
#   Rules:
#       Naming: verbs and keywords
#           Monad: function/argument name should form a verb/noun pair
#                   write(name)
#           Keyword form: encode the names of arguments into the function name
#                   writeField(name)
#                   assertExpectedEqualsActual(expected, actual)
#
#       Flag arguments: Implies function does two things / there should be two functions. Ugly. 
#           Instead of: 
#                   render(multiple_tests)
#           Split into two functions:
#                   renderForSingleTest()
#                   renderForMultipleTests()
#
#       Argument objects:
#           Where arguments are related, they should be wrapped into a class of their own.
#           Bad:
#                   makeCircle(x, y, r)
#           Instead:
#                   makeCircle(center, r)
#
#       Argument lists:
#           Variadic functions take a variable number of arguments.
#           They still should be restricted to monad/dyad/triad form:
#                   monad(Integer... args)
#                   dyad(String name, Integer... args)
#                   triad(String name, int count, Integer... args)
#
#	    Output Arguments:
#	        Arguments are naturally interpreted as inputs to a function. Strongly prefer return for function outputs.
#           If a function must change the state of something, make it the state of its owning object.
#
#       Monadic (1 arg):
#           Asking a question about an argument
#                   bool fileExists(path)
#           Doing something to an argument, and returning the result:
#                   InputStream fileOpen(path)
#           Registering an Event: (use with care)
#                   void logPasswordFailure(attempt_count)
#       Dyadic (2 args):
#           Harder to read than monadic functions, as once must now consider/remember the order of the arguments.
#           Often appropriate (especially where arguments have a natural order):
#                   p = Point(0,0)
#           Bad: no natural ordering of arguments
#                   assert(expected, actual)
#           Alternative: Use name to suggest order
#                   assertExpectedEqualsActual(expected, actual)
#           Convert dyadic functions into monad by using objects:
#                   writeField(outputStream, name_str)
#           vs
#                   outputStream.writeField(name_str)
#           or
#                   writer = Writer(outputStream)
#                   writer.writeField(name_str)
#       Triad (3 args):
#           Use with care, and only when necessary.
#           Sometimes appropriate:
#                   assertFloatEquals(expected, actual, error_allowed)
#           Very Bad:
#                   assertEquals(message, expected, actual)


#	Structured Programming:
#   Dijkstra's rule of structured programming: every block should have one entry/exit.
#   A rule that becomes more important the larger a block/function becomes.

#	How To Approach Writing Functions:
#	First draft code is by nature clumsy and disorganized. Write this code to pass all relevant unit tests, then (applying code-craft principles), refactor and reorganize while continuing to ensure tests pass.


#	Continue: 2022-05-18T02:15:22AEST functions theory, implementation(/better-examples) can come later [...] (another reference for 'what makes a good function' (something online, with better examples to draw from?))
#	Other Examples:

#	LINK: https://github.com/Geeksltd/Programming.Tips/blob/master/docs/methods/stepdown-rule.md
#	{{{
#	Reading Code from Top to Bottom: The Stepdown Rule
#	Code should read like a top-down narrative. Every method should be followed by those at the next level of abstraction so that we can read the program, descending one level of abstraction at a time as we read down the list of methods. I call this The Stepdown Rule.
#	
#	To say this differently, we want to be able to read the program as though it were a set of "To" paragraphs, each of which is describing the current level of abstraction and referencing subsequent TO paragraphs at the next level down.
#	
#	To do A we do B and then C.
#	To do B, if E we do F and otherwise we do G
#	To determine if E, we ...
#	To do F we...
#	To do G we...
#	To do B we...
#	To do C we...
#	Learning to think this way is very important. It is the key to keeping methods short and making sure they do "one thing." Making the code read like a top-down set of TO paragraphs is an effective technique for keeping the abstraction level consistent.
#	
#	Dependent methods: If one method calls another, they should be vertically close in the source file, and the caller should be above the callee where possible. This gives the program a natural flow and enhances the readability of the whole module.
#	
#	The Newspaper Metaphor
#	Think of a well-written newspaper article. You read it vertically.
#	
#	At the top you see a headline that will:
#	
#	tell you what the story is about
#	allow you to decide if you want to read it.
#	The first paragraph gives you a synopsis of the whole story which:
#	
#	Hides all the details
#	Gives you the broad-brush concepts.
#	As you continue downward, the details increase until you have all the dates, names, quotes, claims, and other minutia.
#	We would like a source file to be like a newspaper article
#	The name should be simple but explanatory.
#	The name, by itself, should be sufficient to tell us whether we are in the right module or not.
#	The topmost parts of the source file should provide the high-level concepts and algorithms.
#	Detail should increase as we move downward, until at the end we find the lowest level methods and details in the source file.
#	Would you read a newspaper that is just one long story containing a disorganized agglomeration of facts, dates, and names? A newspaper is composed of many articles, and most are very small. Very rarely articles are a full page long. This makes the newspaper usable.
#	}}}

#	LINK: https://coderanch.com/t/652071/java/line-methods-clean-code
#   {{{
#   {{{
class MainMenu:
    def __init__(self):
        self.availableTeams = [ 'a', 'b', 'c', ]
    def getListOfAvailableTeams(self):
        return self.availableTeams
    def setListOfAvailableTeams(self, newList):
        self.availableTeams = newList
def getNewTeamDescription():
    return "example new team"
#   }}}

#   Example: going too far
class MenuChoiceHandler_i:
    def __init__(self):
        self.mainMenu = MainMenu()
        self.teamToModify = None
        self.teamToModifyIndex = 0
        self.copyOfListOfAvailableTeams = None
    def executeMenuChoice(self):
        self.retrieveAvailableTeams()
        self.getTeamToModify()
        self.setDescriptionOfTeamToModify(getNewTeamDescription())
        self.saveAvailableTeams()
    def retrieveAvailableTeams(self):
        self.copyOfListOfAvailableTeams = self.mainMenu.getListOfAvailableTeams();
    def getTeamToModify(self):
        self.teamToModify =  self.copyOfListOfAvailableTeams[self.teamToModifyIndex];
    def setDescriptionOfTeamToModify(self, newTeamDescription):
        self.teamToModify = newTeamDescription
    def saveAvailableTeams(self):
        self.copyOfListOfAvailableTeams[self.teamToModifyIndex] = self.teamToModify
        self.mainMenu.setListOfAvailableTeams(self.copyOfListOfAvailableTeams)

#   acceptable:
class MenuChoiceHandler_ii:
    def __init__(self):
        self.mainMenu = MainMenu()
        self.teamToModify = None
        self.teamToModifyIndex = 0
        self.copyOfListOfAvailableTeams = None
    def executeMenuChoice(self):
        self.copyOfListOfAvailableTeams = self.mainMenu.getListOfAvailableTeams();
        self.teamToModify = self.copyOfListOfAvailableTeams[self.teamToModifyIndex];
        self.teamToModify = getNewTeamDescription()
        self.copyOfListOfAvailableTeams[self.teamToModifyIndex] = self.teamToModify
        self.mainMenu.setListOfAvailableTeams(self.copyOfListOfAvailableTeams)

#m2 = MenuChoiceHandler_i()
#m2.executeMenuChoice()
#print(m2.mainMenu.availableTeams)
#m2 = MenuChoiceHandler_ii()
#m2.executeMenuChoice()
#print(m2.mainMenu.availableTeams)
#   }}}


#   LINK: https://towardsdatascience.com/12-of-my-favorite-python-practices-for-better-functions-7a21d18cfb38
#   {{{
#   1)  Input/Output
#       Consider what the function does: return or alter something (but not both).
#       Ask: What is neccessary to get there.
#       Then write the function, starting by defining those inputs/outputs.


#   2)  Extraction
#       Creating more methods to handle things that one excessively large function is doing.
#       Functions should be simple, and have short directives. More methods means better code (see below)
#       Guideline: extract anything that cannot be done in 3 lines
#       Shorter functions make bugs easier to narrow down
from numpy import sqrt
def norm_bad(x: list) -> list:
    mu = sum(x) / len(x)
    x2 = [ (i-mu) ** 2 for i in x ]
    m = sum(x2) / len(x2)
    std = sqrt(m)
    return [ (i-mu) / std for i in x ]

def norm_better(x: list) -> list:
    mu = get_mean(x)
    std = get_std(x)
    return [ (i-mu) / std for i in x ]
def get_std(x: list) -> float:
    mu = get_mean(x)
    x2 = [ (i-mu) ** 2 for i in x ]
    m = get_mean(x2)
    return sqrt(m)
def get_mean(x: list) -> float:
    return sum(x) / len(x)

#   3)  Naming
#       A name should describe the output of the function.
#       Ideally, clients should be able to guess what a function is called without even having to check.
#       Well chosen names eliminate the need for many comments.
#       Python uses all-lower-case for method names.
#       <(verbs and keywords: verb describes what the function does/returns, keywords fold arguments into function name)>

#   4)  Avoid Repetition
#       Repeating something in code is a sign that extraction is needed.

#   5)  Less is Superior
#       Less code > More code. 

#   6)  Restrict Types
#       <(But type hints are just that, unless one breaks out 'mypy'?)>
#       <(The article does not talk about validating the input (which is ugly and violates 'less is superior?))>


#   7)  Docstrings
#       <>

#   8)  Minimize nesting
#       Nesting is wherever a new level of scope is created.
#       <(A function should generally not involve more than 2 levels of nesting)>
#       Nested loops should only be used: 1) for prototyping, 2) where there is no alternative


#   9)  Python Decorators
#       <>


#   10) Code your comments
#       Don't comment bad code - rewrite it.
#       Many comments can be made unnecessary by using better names.
#       Do not comment every line of code.


#   11) Use Lambdas
#       Lambdas provide an alternative to declaring a function.
#       Can be mapped to arrays (a more pythonic method than traditional iteration).


#   12) Avoid keyword arguments
#       (These have their place, and it is not everywhere). Prefer positional arguments.

#   }}}

#   LINK: https://towardsdatascience.com/more-methods-means-better-code-1d3b237f6cf2
#   {{{

#   }}}

#   LINK: https://towardsdatascience.com/python-clean-code-6-best-practices-to-make-your-python-functions-more-readable-7ea4c6171d60
#   {{{
#   }}}
#	LINK: https://towardsdatascience.com/a-walkthru-for-writing-better-functions-6cb37f2fa58c
#	{{{
#	}}}
#	LINK: https://towardsdatascience.com/comprehensive-guide-to-writing-python-functions-others-can-use-2fa186c6be71
#	{{{
#	}}}
#	LINK: https://epirhandbook.com/en/writing-functions-1.html
#	{{{
#	}}}
#	LINK: https://en.wikipedia.org/wiki/SOLID
#	{{{
#	}}}
#	LINK: https://dev.to/levivm/coding-best-practices-chapter-one-functions-4n15
#	{{{
#	}}}
#	LINK: https://www.quora.com/What-are-some-best-practices-in-defining-function-or-method-parameters-in-programs
#	{{{
#	}}}
#	LINK: https://www.reddit.com/r/coding/comments/9yfv4/best_practice_should_functions_return_null_or_an/
#	{{{
#	}}}


#   Summary:
#       Functions should be short. They should be even shorter than that.
#       <(Anything that cannot be done in 3 lines should be extracted)>
#       <>

