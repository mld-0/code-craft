#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
import sys
import os
#   {{{2
#   Ongoing: 2022-06-10T01:52:42AEST the 'Visitor' pattern

#   English Terminology:
#   {{{
#   noun: a thing
#   verb: an action or state-of-being
#   adjective: describes or changes a noun 

#   verb-phrase: a verb and its arguments, excluding the subject
#           Yankee batters (hit the ball well enough to win their first World Series since 2000)
#           Mary (saw the man through the window)
#           David (gave Mary a book)

#   noun-phrase: a phrase, surrounding a noun, that serves the role of a noun
#           (Current economic weakness) may be (a result of high energy prices)
#           (Almost every sentence) contains (at least one noun phrase)
#           (The subject noun phrase that is present in this sentence) is long

#   noun-adjunct: an optional noun that modifies another noun, similar to an adjective
#   That is, a noun functioning as a pre-modifier in a noun-phrase.
#           (Chicken) soup
#           (Field) player

#   modal verb: indicates a <(modality: relationship to reality or the truth)> 
#           can/could/may/might/shall/should/will/would/must 

#   participle: word based off a verb that expresses a state-of-being that functions as an adjective (ending in 'ing', 'ed', ect) (modifies a noun)

#   determiner: express the <(reference: link between objects)> of a noun in context
#   {{{
#           articles:		                the/a/an 
#           demonstratives:		            this/that 
#           possesive determiners:		    my/their 
#           quantifiers:		            many/all/no 
#           distributive:		            each/any
#           interrogative:		            which
#   }}}

#   singular noun: refers to one person, place, or thing
#   plural noun: refers to multiple things

#   collective noun: a group taken as a whole
#           choir, galaxy

#   transitive verb: verb that requires an object to recieve the action
#   direct noun: noun that is directly affected by action of a verb

#   <>

#   }}}

#   Names are everywhere in software. 
#   Names should reveal intention. 
#   If a variable needs a explanatory comment, then its name does not reveal its intent.
#   Good names are an essential part of clean code. Take some time to chose good names, and replace them with better ones when they arise.

#   Avoid disinformation: Don't use words whose entrenched meaning varies from our intended meaning.
#   Avoid noise words. Make meaningful distinctions. 
#   Beware of names which only vary in small ways.
#   Don't make arbitrary changes to names. Don't use incorrect spellings.
#   Avoid encoding type/scope information.
#   Avoid prefixes, enclose variables in classes/namespaces instead.

#   Example: intention revealing vs meaningless names
#           copyChars(a1, a2)
#           copyChars(src, dest)

#   Example: names without meaningful distinctions become interchangeable
#           Product
#           ProductInfo
#           ProductData

#   'table' should never appear in a table name. 'object' should never appear in an object name.

#   The length of a name should correspond to the size of its scope.
#   Names should be easy to search in a body of text.

#   Avoid literal constant values. Use named variable instead.
#   Avoid names that place any extra mental burden on the reader. 
#   Single letter names are a poor choice in most contexts.
#   Clarity is king. Say what you mean. Mean what you say.

#   Interfaces and Implementations: (suggestion), leave interface unadorned.
#           interface:          ShapeFactory
#           implementation:     ShapeFactoryImpl

#   Class Names: nouns or noun-phrases. Not a verb.
#   Start with upper, camelCase.
#           Customer
#           WikiPage
#           Account
#           AddressParser

#   Method names: verb or verb-phrase
#   Start with lower, camelCase
#           postPayment
#           deletePage
#           save
#   Use get/set/is for accessors/mutators/predicates. Use the same word to describe the same action each time.
#   <(Verb-phrase: a verb and its arguments, excluding the subject noun)>

#   Variables: python advises snake_case for variables (to differentiate them from classes/methods)
#   snake_case is arguably easier to read.

#   Constants:
#   Screaming snake case
#   Avoid magic numbers, name all constants.
#           MAX_COUNT
#           USER_NAME_FIELD

#   Make overloaded constructors private, and create static factory methods with names describing the arguments:
#           auto p = Complex.FromRealNumber(23.0)

#   Don't use multiple different words for the same concept. Don't use the same word for two different concepts. Don't use similar words interchangeably. Be consistent. 

#   Prefer solution domain names to problem domain names. Use technical names as appropriate.
#   Separate problem and solution domain concepts.

#   Enclose names in a meaningful context. Don't add redundant/irrelevant context. 

#   'Address' is a suitable name for a class where it is not necessary to distinguish between types of addresses. 'PostalAddress' / 'MAC' / 'URL' are suitable class names to distinguish between types of addresses.

#   Put the most important word on the left:
#           Bad         Push this button to lift the exit gate
#           Good        To lift the exit gate, push this button

#   Defer to guidelines of language in question.


#   Prefer 'Modifier-Subject', but use 'Subject-Modifier' wherever it is more readable
#   LINK: https://softwareengineering.stackexchange.com/questions/160370/order-of-subject-and-modifiers-in-variable-names
#   {{{
#   <(We come here asking: count_written or written_count?)>
#   <(If we (might) have multiple count_, that is the subject, if we have multiple written_, that is the subject?)>
#   <(If we have multiple of neither [...] 'count' is the subject?)>

#   Questions to ask: What is the subject and what is the modifier?
#   <>

#   Subject-Modifier:           Modifier-Subject 
#       AreaAdujusted               AdujstedArea
#       AreaInnerSurface            SurfaceAreaInner
#       AreaOuterSurface            SurfaceAreaOuter
#   In this case, both are bad: use Area[region] instead

#   Assertions: 
#   Modifier-Subject, (since that is generally better English) unless Subject-Modifier is better English.
#   Subject-Modifier is something designers do only to satisfy IntelliSense.
#   Having difficulty with long lists in intellisense isn't a variable naming problem, it's a class size problem. 
#   Never use a particular coding convention only to satisfy your programming environment.
#   Use the word order you'd use when writing it in normal English. If you have multiple such prefixed properties, fields (and methods), consider putting those members together in a related class

#   Which is the modifier: wallThickness
#           If working with walls, 'thickness' is the modifier (and varname should be 'thicknessWall')
#           If working with thicknesses, 'wall' is the modifier 

#   There is no always-best-option, consider:
#   Which order is most likely to leave the reader with the correct purpose of the variable?
#   Which order is better english?

#   Consider: timeStart vs startTime
#   (We presumedly must also have endTime, elapsedTime)
#   <(We are working with times, hence 'start' is the modifier)>
#   

#   As a general rule 'written_count' is the better variable name ... in this case, I contend 'count_written' is better
#   }}}


#   LINK: https://dev.to/somedood/a-grammar-based-naming-convention-13jf
#   {{{
#   Prefer camelCase to snake_case

#   Use SCREAMING_CASE for contants
#   A true constant is a static value that does not depend on runtime values

#   Name indervidual objects with the most apropriate singular noun

#   Booleans should be prefixed with is/has/can/similar

#   Arrays/containers should be named a plural noun, or a collective noun if that is more readable

#   Functions: A verb, or verb + noun (where the verb/noun pair refer to each other)
#           GetProccess()
#           WhereObject()
#           MeasureObject()

#   Class: Proper noun in PascalCase

#   Fields: As per variables
#   Methods: omit noun of 'verb+noun' pair where object name fills its place

#   Example:
#       const TRUE_CONSTANT = Math.PI;
#       const stringName = '';
#       const numberName = 0;
#       const isBooleanName = true;
#       const objName = { };
#       const arrayNames = [ ].map(name => name);
#       function getFunctionName() { }
#       class ClassName { }

#   }}}


#   LINK: https://github.com/kettanaito/naming-cheatsheet
#   {{{
#   Use English
#   Use one naming convention, and be consistent

#   S-I-D: Short, Intuitive, Descriptive

#   Do not use contractions
#   Avoid context duplication
#   Reflect the expected result

#   Functions:
#   (P)A/HC/LC   (prefix?) + action + high-context + low-context
#
#   prefix: enhances the meaning of a function
#       is: (boolean) characteristic of a context
#       has: (boolean) whether the context possesses a value/state
#       should: (boolean) of a certain action
#       min/max: describing boundaries or limits
#       prev/next: state transitions
#
#   action: verb part of function name
#       get: access internal data
#       set: set internal data
#       reset: restore initial state
#       fetch: request which takes time
#       remove: remove an item from a collection
#       delete: erase/destroy a thing
#       compose: create new data from existing data
#       handle: handle an action (callback method)
#
#   context: a domain the function operates on. 
#   
#   high context: emphasizes the meaning of a variable
#   low context: <?>
#
#       Name:                   Prefix      Action (A)      High-context (HC)       Low-context (LC)
#       getPost                             get             Post
#       getPostData                         get             Post                    Data
#       handleClickOutside                  handle          Click                   Outside
#       shouldDisplayMessage    should      Display         Message

#   }}}


#   LINK: https://en.wikipedia.org/wiki/Naming_convention_(programming)
#   {{{
#   }}}


