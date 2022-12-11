#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   }}}

#   Two types of objects
#       Service objects: either perform a task or return a piece of information
#       Material (data) objects: hold data, present methods for accessing/manipulating that data

#   <(Service objects are generally immutable)>
#   Created once, run once/repeatedly/forever

#   Service objects typically have names indicating what they do:
#       controller / renderer / calculator


#   Inject dependencies / configuration-values as ctor arguments:
#   A service usually needs other services or configuration values to do its job.
#   These should be provided as ctor arguments (leaving the service ready for use after the ctor call)
#   Provide only those services/parameters the object needs (avoid supplying entire config objects where unneccessary)


#   Keep configuration values together that belong together:
#   (Introduce dedicated configuration objects containing them all)

#   Whenever a service needs another service in order to perform its task, it should declare the latter explicitly as a dependency and get it injected as a constructor argument


#   Inject what you need, not where you can get it from:
#   Have the actual dependency as argument, not a class containing it.
#   That is, require:
#           user.getByID(request.get('userID'))
#   not:
#            user.getByID(request)


#   All constructor arguments should be required:
#   (This avoids ambiguity about what has been provided)


#   Do not use setter methods, supply dependencies only through the ctor:
#   (It shouldn't be possible to create incomplete service objects)
#   (Service objects should be immutable)


#   There is no such thing as an optional dependency


#   Make all dependencies explict:
#   A service ctor should not retrive globally available dependencies
#   They should be ctor arguments the caller is required to pass





