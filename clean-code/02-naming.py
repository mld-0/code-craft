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
#   {{{
#           Yankee batters (hit the ball well enough to win their first World Series since 2000)
#           Mary (saw the man through the window)
#           David (gave Mary a book)
#   }}}

#   noun-phrase: a phrase, surrounding a noun, that serves the role of a noun
#   {{{
#           (Current economic weakness) may be (a result of high energy prices)
#           (Almost every sentence) contains (at least one noun phrase)
#           (The subject noun phrase that is present in this sentence) is long
#   }}}

#   determiner: express the <(reference: link between objects)> of a noun in context
#   {{{
#       articles:		                the/a/an 
#       demonstratives:		            this/that 
#       possesive determiners:		    my/their 
#       quantifiers:		            many/all/no 
#       distributive:		            each/any
#       interrogative:		            which
#   }}}

#   modal verb: indicates a <(modality: relationship to reality or the truth)> can/could/may/might/shall/should/will/would/must 

#   participle: word based off a verb that expresses a state-of-being that functions as an adjective (ending in 'ing', 'ed', ect) (modifies a noun)

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
#           Customer
#           WikiPage
#           Account
#           AddressParser

#   Method names: verb or verb-phrase
#           postPayment
#           deletePage
#           save
#   Use get/set/is for accessors/mutators/predicates. Use the same word to describe the same action each time.
#   <(Verb-phrase: a verb and its arguments, excluding the subject noun)>

#   Make overloaded constructors private, and create static factory methods with names describing the arguments:
#           auto p = Complex.FromRealNumber(23.0)

#   Don't use multiple different words for the same concept. Don't use the same word for two different concepts. Don't use similar words interchangeably. Be consistent. 

#   Prefer solution domain names to problem domain names. Use technical names as appropriate.
#   Separate problem and solution domain concepts.

#   Enclose names in a meaningful context. Don't add redundant/irrelevant context. 

#   'Address' is a suitable name for a class where it is not necessary to distinguish between types of addresses. 'PostalAddress' / 'MAC' / 'URL' are suitable class names to distinguish between types of addresses.


#   <(resources?)>

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

