#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2

#   Ongoings:
#   {{{
#   2023-08-27T22:14:40AEST object creation: instantiation of an object, object composition: building complex objects by supplying simpler ones (to be member variables)
#   }}}

#   Creation design-patterns abstract the instantiation of object. They:
#       - help make a system independent of how objects are created, composed, and represented
#       - become more important in the context composition as the total number of objects increases
#       - encapsulate knowledge about how objects are created
#       - encapsulate knowledge about which [{concrete}] classes a system [{uses/requires}]

#   [{They allow a system to be configured with 'product' objects (which can vary widely in structure and functionality). This configuration can be static (made at compile-time) or dynamic (made at runtime)}]

#   Creation design-patterns include:
#           - Abstract Factory
#           - Factory Method
#           - Builder
#           - Prototype
#           - Singleton
#   {{{
#   Relationships between patterns:
#   Prototype and Abstract Factory are generally exclusive
#   Builder can use another creation design-pattern to [{implement which component gets built}]
#   Prototype can use Singleton in its implementation
#   }}}


#   Case Study: CreateMaze
#   {{{
#   }}}


