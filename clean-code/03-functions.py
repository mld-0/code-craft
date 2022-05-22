#	VIM SETTINGS: {{{3
#	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#	vim: set foldlevel=2 foldcolumn=2:
#	}}}1
import sys
import os
import logging
import typing
from io import StringIO
#	{{{2
#   log(): get class name logger
#   {{{
LOGGING_FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
LOGGING_FORMAT = "%(levelname)-8s %(name)s.%(funcName)s: %(message)s"
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format=LOGGING_FORMAT)
def log():
    """Return logger specific to callee class (or default logger if caller not a class)"""
    #   {{{
    try:
        stack = inspect.stack()
        logger_classname = stack[1][0].f_locals["self"].__class__.__name__
        return logging.getLogger(logger_classname)
    except KeyError as ex:
        return logging.getLogger()
    #   }}}
#   }}}
#   Ongoings:
#	{{{
#	Ongoing: 2022-05-20T19:50:22AEST expand/provide-definitions until source is compile-able
#	Ongoing: 2022-05-20T18:56:57AEST C++ makes this (step-down) rule a PITA, requiring functions to be declared before they are used
#	Ongoing: 2022-05-20T18:57:19AEST C++, observing the step-down rule in a language wehre every function must be declared before it is used
#	Ongoing: 2022-05-18T03:08:47AEST a hierachy to functions (namespaces? classes?), beyond simply having function explosion at global scope (how would one do it for book examples?) (see above)
#	Ongoing: 2022-05-20T18:33:18AEST (there must be) a better before/after example than what the book presents?
#	Ongoing: 2022-05-20T18:46:02AEST is 'isTestPage()' (as its own function) really necessary?
#	}}}

#	TODO: 2022-05-18T02:12:01AEST code-craft/clean-code/03-functions, plausible data-flow / roles for each object, complete example doing something that makes calls of 'renderPageWithSetupsAndTeardowns' make sense
#   TODO: 2022-05-21T06:18:14AEST code-craft/clean-code/03-functions, verification/enforcing of python type hints (primative/custom types)
#	Continue: 2022-05-18T23:48:43AEST example 'renderPageWithSetupsAndTeardowns' is later explored implemented as a class (called 'uncle_bob' in book source)


#	Functions implement subroutines in modern languages. 
#	They are the first line of organization in any program.

#	LINK: https://coderanch.com/t/652071/java/line-methods-clean-code
#   {{{
#   }}}

#	Example: renderPageWithSetupsAndTeardowns (book) from 'FitNesse' function
#   {{{
#	<(Done by method extracting / renaming / restructuring first horror-show example)>
#	<(Setup/Teardown test cases run before/after regular test cases respectively)>
##	{{{
#string renderPageWithSetupsAndTeardowns(PageData& pageData, bool isSuite) {
#	bool isTestPage = pageData.hasAttribute("test");
#	if (isTestPage) {
#		//	<contents?> from PageData 
#		WikiPage testPage = pageData.getWikiPage();
#		//	<vector of strings>
#		stringstream newPageContent;
#		//	<(putting stuff (settings?) from pageData -> testPage -> newPageContent)>
#		includeSetupPages(testPage, newPageContent, isSuite);
#		//	putting pageData.contents -> newPageContent
#		newPageContent << pageData.getContent();
#		//	<(putting(?) )>
#		includeTeardownPages(testPage, newPageContent, isSuite);
#		//	newPageContent -> pageData
#		pageData.setContent(newPageContent.str());
#	}
#	return pageData.getHtml();
#}
##	A function should do one thing: this function is doing 3: 
##			1) determine whether 'pageData' is a test page
##			2) if so, include setups/teardowns
##			3) render the page in html
##	}}}

##   typing forward declarations: [...] (don't work with mypy) 
#Blah = typing.NewType("Blah", None)
#VirtualEnabledPageCrawler = typing.NewType("VirtualEnabledPageCrawler", None)
#WikiPage = typing.NewType("WikiPage", None)
#WikiPagePath = typing.NewType("WikiPagePath", None)
#PageData = typing.NewType("PateData", None)
#   <(alternative solution: provide type name as string?)>

class PageCrawler: 
    #   {{{
    def setDeadEndStrategy(self, virtualEnabledPageCrawler: 'VirtualEnabledPageCrawler'):
        pass
    def getPage(self, root: 'Blah', path: 'WikiPagePath') -> 'WikiPage':
        raise NotImplementedError()
    def getFullPath(self, page: 'WikiPage') -> 'WikiPagePath':
        raise NotImplementedError()
    #   }}}

class Blah:
    #   {{{
    def getPageCrawler(self) -> PageCrawler:
        raise NotImplementedError()
    #   }}}

class WikiPage:
    #   {{{
    def getData(self) -> 'PageData':
        raise NotImplementedError()
    def getPageCrawler(self) -> 'PageCrawler':
        raise NotImplementedError()
    def getFullPath(self, page: 'WikiPage') -> 'WikiPagePath':
        raise NotImplementedError()
    #   }}}

class VirtualEnabledPageCrawler:
    pass

class WikiPagePath:
    pass

class PageData: 
    #   {{{
    def __init__(self):
        self.str_list = []
    def getWikiPage(self) -> 'WikiPage':
        raise NotImplementedError()
    def hasAttribute(self, test: str) -> bool:
        raise NotImplementedError()
    def getContent(self) -> str: 
        return ""
    def getHtml(self) -> str:
        return ""
    def setContent(self, s: StringIO):
        s.seek(0)
        new_content = s.read()
        #   Ongoing: 2022-05-21T07:12:26AEST get logging.debug() to include class.method in output (or f----- specify it all manually (oh lawrdy have mercy at that point aren't you better just wrapping logging?
        #   {{{
        #   Continue: 2022-05-21T08:47:02AEST a major diversion -> how to provide 'log()' that includes caller function name and class (see python-examples/py-logging-classname)
        #logging.debug("(new_content)=(%s)" % new_content)
        #   }}}
        log().debug("new_content=(%s)" % new_content)
        self.str_list.append(new_content)
    #   }}}

def renderPageWithSetupsAndTeardowns(pageData: PageData, isSuite: bool) -> str: 
    if isTestPage(pageData): 
        includeSetupAndTeardownPages(pageData, isSuite)
    return pageData.getHtml();

def isTestPage(pageData: PageData) -> bool: 
    return pageData.hasAttribute("test")

def includeSetupAndTeardownPages(pageData: PageData, isSuite: bool):
    testPage = pageData.getWikiPage()  #   WikiPage 
    newPageContent = StringIO()
    includeSetupPages(testPage, newPageContent, isSuite)
    newPageContent.write(pageData.getContent())
    includeTeardownPages(testPage, newPageContent, isSuite)
    pageData.setContent(newPageContent)

def includeSetupPages(testPage: WikiPage, newPageContent: StringIO, isSuite: bool):
    raise NotImplementedError()

def includeTeardownPages(page: WikiPage, content: StringIO, isSuite: bool):
    raise NotImplementedError()

#   }}}


#	Rule 1: Small
#	The first rule of functions is that they should be small. (The second rules is they should be even smaller than that. Functions should hardly ever be 20 lines long).
#	Blocks within if/else/for/while statements should be one line long (probably a function call).
#	This adds documentary value, because every block gets a descriptive name.
#	Limit nested structures, ideally not more than 2 levels.


#	Rule 2: Do One Thing
#	Functions should do one thing. They should do it well. They should do it only. 
#	The purpouse of a function is to decompose a larger concept (described by function name) into steps at the next level of abstraction.
#	If a function does only those steps that are one level below the stated name of the function, then the function is doing only one thing. 
#	Or: <(If one can extract another function with a name that is not merely a restatement of the containing functions implementation, that function is doing more than one thing)> <(Functions that do one thing cannot be reasonably divided into sections)>



#	LINK: https://dzone.com/articles/slap-your-methods-and-dont-make-me-think

#	Rule 3: One level of abstraction per function
#	Mixing levels of abstraction is always confusing. 
#	<(It makes unclear what is an essential concept and what is a detail. When essential concepts and details are mixed in a function, more and more details tend to accumulate in that function.)>

#	Example: mixed levels of abstraction
class Food:
    pass
class FryingPan:
    #   {{{
    def getServing(self, percentage: int) -> Food:
        raise NotImplementedError()
    #   }}}
class Plate:
    #   {{{
    def addFood(self, food: Food):
        raise NotImplementedError()
    #   }}}
class BreakfastMaker:
    #   {{{
    def __init__(self):
        wife = Plate()
        husband = Plate()
        fryingPan = FryingPan()
    def cook(self):
        raise NotImplementedError()
    def serve(self):
        raise NotImplementedError()
    #   }}}

    #	Bad: mixed levels of abstraction
    def makeBreakfast_bad(self):
        cook()
        plate_wife.give(fryingPan.getServing(20))
        plate_husband.give(fryingPan.getServing(80))

    #	Fixed: each lower level of abstraction moved to its own function
    def makeBreakfast_good(self):
        cook()
        serve()


#	Rule 4: The Stepdown Rule
#	Code should read like a top-down narrative, higher levels of abstraction above lower ones.
#	Or, caller functions should reside above callee functions.
#	<(Where the lower-level function is used by two/more higher level functions: place it below the last usage)>


#	LINK: https://dzone.com/articles/the-stepdown-rule
#	{{{
#	Ongoing: 2022-05-20T19:58:07AEST Consider, the stepdown rule and the case of 'keep similar (high-level) functions together' (I say the example is wrong) (see below) [...] (a hybrid approach, keep public functions together?)
#	bad (supposedly?)
#			void MakeBreakfast()
#			void MakeDinner()
#			private void cookBreakfast()
#			private void cookDinner()
#			private void serveBreakfast()
#			private void serveDinner()
#			private void cleanup()
#	good (supposedly?)
#			void MakeBreakfast()
#			private void cookBreakfast()
#			private void serveBreakfast()
#			void MakeDinner()
#			private void cookDinner()
#			private void serveDinner()
#			private void cleanup()



#	}}}


#	Rule 5: Descriptive names
#	<>


#	(Alternatives to switch statement: the AbstractFactory)
#	<>


#	Function Arguments:
#	<>


#	Have No Side Effects:
#	<>

#	Output Arguments:
#	<>


#	Command Query Seperation:
#	<>


#	Prefer Exceptions to Error Codes:
#	<>


#	Extract Try/Catch Blocks:
#	<>


#	Error handling is One Thing:
#	<>


#	Don't Repeat Yourself:
#	<>


#	Structured Programming:
#	<>


#	How To Approach Writing Functions:
#	<>


#	Other Examples:
#	Continue: 2022-05-18T02:15:22AEST functions theory, implementation(/better-examples) can come later [...] (another reference for 'what makes a good function' (something online, with better examples to draw from?))

#	LINK: https://github.com/Geeksltd/Programming.Tips/blob/master/docs/methods/stepdown-rule.md
#	{{{
#	Reading Code from Top to Bottom: The Stepdown Rule
#	Code should read like a top-down narrative. Every method should be followed by those at the next level of abstraction so that we can read the program, descending one level of abstraction at a time as we read down the list of methods. I call this The Stepdown Rule.
#	
#	To say this differently, we want to be able to read the program as though it were a set of “To” paragraphs, each of which is describing the current level of abstraction and referencing subsequent TO paragraphs at the next level down.
#	
#	To do A we do B and then C.
#	To do B, if E we do F and otherwise we do G
#	To determine if E, we …
#	To do F we …
#	To do G we...
#	To do B we…
#	To do C we…
#	Learning to think this way is very important. It is the key to keeping methods short and making sure they do “one thing.” Making the code read like a top-down set of TO paragraphs is an effective technique for keeping the abstraction level consistent.
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

#	LINK: https://towardsdatascience.com/a-walkthru-for-writing-better-functions-6cb37f2fa58c
#	LINK: https://towardsdatascience.com/comprehensive-guide-to-writing-python-functions-others-can-use-2fa186c6be71
#	LINK: https://epirhandbook.com/en/writing-functions-1.html

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


