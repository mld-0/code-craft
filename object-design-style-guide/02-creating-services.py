#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   Ongoing: 2023-01-14T22:58:00AEDT ctor with object to provide sensible deaults 'Logger(new DefaultLoggerConfig())' vs factory function to provide sensible defaults 'Logger.createDefault()'(?)
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


#   Make all dependencies explict:
#       Do not use setter methods, supply dependencies only through the ctor:
#       (It shouldn't be possible to create incomplete service objects)
#       (Service objects should be immutable)
#       There is no such thing as an optional dependency
#       A service ctor should not retrive dependencies itself, even if they are globally available (require the caller to pass them as ctor arguments)
#       If a service object will oftern be created with given default values, use a factory method, not the default ctor, to create an object with those default values.

#   Allow for dummy object in ctor
#           logger = new Logger(new NullLogger())
#   Object to provide sensible defaults
#           logger = new Logger(new DefaultLoggerConfig())
#   Factor function to provide sensible defaults
#           logger = Logger.createDefault()

#   Turn static dependencies into object dependencies:
#       Do not get dependencies from globally available accessors
#       Instead require that they be passed as ctor arguments

#   <(If a service uses complicated functions, consider placing a wrapper class around them, if:)>
#           We wish to replace/enhance these functions at some later point
#           <(Is there a certain level of complexity to the behavior of this dependency, such that you couldn't achieve the same result with just a few lines of custom code?)>
#           If the function dealing with objects (not primatives)


#   <(Move system calls outside the class)>
#   eg:
#           meetupRepository = new MeetupRepository(new SystemClock())



#   Task-relevent data should be passed as method arguments (not ctor arguments)
#       Pass service object depencencies/config as ctor arguments
#       Pass task relevent information as method arguments 


#   Don't allow behaviour of a service to change after it has been instantiated
#   (allow such behaviour to be configured only by the ctor)


#   Do nothing in the ctor besides assign properties
#   A service object should not do anything until a method is called
#   (If it is necessary to setup an object, consider using a factory function)


#   Throw an exception when an argument is invalid
#   Do not allow an object to be constructed with invalid parameters


#   Define services as an immutable object graph with only few entry points
#   All services of an application combined will form a large, immutable object graph, often managed by a service container. Controllers are the entry points of this graph. Services can be instantiated once and reused many times.



#   Summary:
#       Two types of objects, service/data-structure
#       Inject dependencies/config-values (only) as ctor arguments (and do not allow them to change)
#       Inject what you need, not where you can get it from
#       All ctor arguments should be required
#       There is no such thing as an optional dependency
#       Make all dependencies explict 
#       Task relevent data should be passed as method arguments, not ctor arguments
#       Do not allow the behaviour of a service to change after it has been instantitated
#       Do nothing in the ctor besides assign properties
#       Throw an exception when an argument is invalid
#       Define services as an immutable object graph with only few entry points

