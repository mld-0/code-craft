//	vim: set tabstop=4 modeline modelines=10:
//	vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
//	{{{2
//	Ongoings:
//	{{{
//	Ongoing: 2022-05-31T01:08:31AEST seeing the 'hierarchy of class implementation' (pre-perquisite classes for a class) where inheritance is not used (nicely listing them all in one place when using composition rather than inheritance) [...] (and inheritance vs composition (generally) re: said example)
//	Ongoing: 2022-05-31T01:30:32AEST being pedantic about the use of the word 'object' vs 'class'
//	Ongoing: 2022-06-02T23:00:26AEST C++, overriding Derived class member variables? [...] (one cannot override variables, declaring a variable of the same name in Derived hides the Base variable)
//	Ongoing: 2022-06-03T02:28:48AEST what is meant by 'efficent procedure' (is just a little bit to obvious of-a beside-the-point rabbit hole)
//	Ongoing: 2022-06-03T04:58:56AEST my <question/problem>: Composition doesn't provide a nice list of parent/dependent classes the way inheritance does(?) <(consider C++ and Python - how to get them?)>
//	}}}

//	Background:
//	{{{
//	Other Programming Paradigms:
//		Imperative (Pascal, C)
//		Logic (Prolog)
//		Functional (ML, Haskell)

//	OOP first gained notoriety in the 1980s.
//	(Book Propositions):
//	OOP is a revolutionary idea, unlike anything that came before it
//	OOP is an evolutionary step, following naturally from earlier programming abstractions

//	OOP is a paradigm that scales very well, providing abstraction and hierarchy that represents many real-life problems.
//	It is also tends to lead to the 'If your tool is a Hammer' fallacy.
//	<(Everything is an object (is a lie?))>

//	Example: (switching to a different paradigm leading to a better solution) DNA sequence as a vector of N integers, discover whether any pattern of length M is ever repeated.
//	{{{
//	
//	O(M * N**2):
//	     DO 10 I = 1, N-M
//	      DO 10 J = 1, N-M
//	      FOUND = .TRUE.
//	      DO 20 K = 1, M
//	  20  IF X[I+K-1] .NE. X[J+K-1] THEN FOUND = .FALSE.
//	      IF FOUND THEN ...
//	10 CONTINUE
//
//		vs:
//	
//	O(M*N*ln(N))
//		APL, matrix of N rows / M columns, sort by rows, check for duplicate rows
//	
//	}}}

//	Church's conjecture: any computation for which there is an efficient procedure can be realized by a Turing Machine
//	Sapir-Whorf hypothesis: it may be possible for an individual working in one language to utter ideas that cannot be translated (or even understood) by individuals working in another <linguistic-framework>.
//	<(A question of ideas vs implementation?)>
//	The choice of language will *direct* thoughts, but it cannot *proscribe* (inhibit/prevent) thoughts
//	}}}

//	An object will normally carry out an action by delegating-to/calling-on other objects. 
//	This is a natural fit for the kind of re-use that needed for modern software development.
//	A key aspect of OO-programs is information hiding - objects make an interface available to callers and keep their implementation hidden.

//	Agents and communities:
//	OO-programs are structured around a community of objects interacting by making requests.
//				Agent: 		an object <(sending/recieving? request)>
//				Action: 	initiated through transmission of message to 'agent' (object responsible for action)
//				Message: 	a method call with accompanying arguments
// (Designated) Receiver: 	accepts responsibility for message, carries out the requested action
//				Method: 	responsible for carrying out the requested action


//	Message vs Procedural call:
//	A message (method call) has a designated receiver, whereas a procedure call does not.
//	The interpretation of the message is determined by the receiver (different classes can define different versions of the same function (in which case late binding is performed with the code to be called) (whereas the call to a procedure is bound early).


//	Responsibilities:
//	(How to) carry out requests is the (solely) the responsibility of the receiver. 
//			Protocol: the set of responsibilities associated with an object


//	Procedural vs OO:
//	A procedural program often involves running procedures on data-structures.
//	An OO program involves making requests of objects (data-structures) to perform a service.


//	Classes and instances:
//	All objects are instances of a class. 
//	All objects of the same class use the same method to respond to similar messages.


//	Class Hierarchies - Inheritance:
//	Child classes (subclasses) inherit attributes of their parent class(es).
//	<(effective-c++: public inheritance models is-a)>
//	An abstract class is a class which cannot be instantiated, it is only for creating subclasses.

//	Class Hierarchies - Composition:
//	<>

//	Method binding and overriding:
//	Encode exceptions to a general rule by overriding information inherited from parent class
//	Different objects using different methods to handle the same request is Polymorphism.
//	<(effective-c++: don't override non-virtual functions)> <(don't override variables (because you can't), and don't hide them either?)>

//	Example: hierarchy of class implementation
//		RobinFlorist: DeliveryPerson, FlowerAranger, Wholesaler
//			DeliveryPerson: Robin
//				Robin: Person
//			Wholesaler: Grower
//				Grower: Gardeners

//	OOP-Summary:
//		Everything is an object. 
//		Computation is performed by objects sending/receiving messages (requests for action).
//		A message takes the form of a function call with/without arguments.
//		Each object has its own memory, which consists of other objects.
//		Each object is an instance of a class.
//		<(A class simply represents a grouping of similar objects, such as integers or lists)>
//		A class defines behaviour (methods) associated with that type of object.
//		Classes are organized into an inheritance hierarchy. 
//		<(Public inheritance models is-a)>.
//		<(Composition and private inheritance model has-a)>.


//	Computation as Simulation
//	Traditional model describing a program is a 'process-state' or 'pigeon-hole' model.
//	This involves details such as memory addresses, <?>
//	In contrast, in OOP we never mention memory addresses, variables, assignments, ect: Instead, we speak of objects, messages, and responsibility for some action.
//	This view of programming is that we are creating a 'universe', or 'discrete event-driven simulation'.
//	That is, through OOP, computing becomes a simulation.

//	(OOP lends itself to) The Power of the Metaphor 
//	<(And then along comes a rather dumb Mr Potato Head analogy?)>

//	Avoiding infinite regression:
//	Objects cannot be implemented in terms of other objects forever, at some point, an object must provide the implementation in a non-OO manner. For this, OO languages make 'primative' datatypes available (either directly coresponding to the machine's primatives (eg: C++), or as higher level primative/native operations of the language (eg: python).
//	(The takeaway is): OO-languages need to provide procedural syntax and primative data types.

//	A Brief History of OOP:
//	{{{
//	Simula (1960s)
//	Smalltalk (1980s)
//	C-with-classes (1980s)
//	C++ (1990s)
//	Then come Java/C#, and the rest is history
//	}}}

//	(Book) Further reading (section)(?)
//	<>

//	LINK: https://realpython.com/inheritance-composition-python/
//	{{{
//	<>

//	Guidelines:
//	Use inheritance over composition in Python to model a clear is a relationship. First, justify the relationship between the derived class and its base. Then, reverse the relationship and try to justify it. If you can justify the relationship in both directions, then you should not use inheritance between them.
//	Use inheritance over composition in Python to leverage both the interface and implementation of the base class.
//	Use inheritance over composition in Python to provide mixin features to several unrelated classes when there is only one implementation of that feature.
//	Use composition over inheritance in Python to model a has a relationship that leverages the implementation of the component class.
//	Use composition over inheritance in Python to create components that can be reused by multiple classes in your Python applications.
//	Use composition over inheritance in Python to implement groups of behaviors and policies that can be applied interchangeably to other classes to customize their behavior.
//	Use composition over inheritance in Python to enable run-time behavior changes without affecting existing classes.

//	Links / (book recomendations)
//	Design Patterns: Elements of Reusable Object-Oriented Software
//	Head First Design Patterns: A Brain-Friendly Guide
//	Clean Code: A Handbook of Agile Software Craftsmanship
//	LINK: https://en.wikipedia.org/wiki/SOLID
//	LINK: https://en.wikipedia.org/wiki/Liskov_substitution_principle
//	}}}

int main()
{
	return 0;
}

//	Summary:
//		OOP is way of thinking about decomposing problems and developing solutions (not just a set of language features).
//		OOP views a program as a collections of agents called objects. Each object is responsible for a specific task. It is by the interaction of objects that computation procedes. In this sense, OOP is analogous to a simulation.
//		An object is an encapsulation of state (data) and behaviour (code). It is analogous to a special purpouse <container/computer>.
//		The behaviour of objects is dictacted by the objects class. All objects of the same class exhibit the same behaviour.
//		All objects are instances of some class.
//		The behaviour of an object is defined by its methods, which are invoked by caller messages.
//		Classes may be linked through inheritance. Public inheritance models 'is-a'. Private inheritance models 'is-implemented-in-terms-of'.
//		<(Composition?)>
//		An OO-Program is like a community of inderviduals, each given certain responsibilities. 
//		OOP allows reduces interdependency among software components, facilitating testing and reuse
//		OOP permits the programmer to deal with a higher level of abstraction.

