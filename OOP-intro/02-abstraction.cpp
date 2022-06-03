//	vim: set tabstop=4 modeline modelines=10:
//	vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
//	{{{2

//	Abstraction: purposeful suppression of some details to bring out others more clearly.
//	Information Hiding: purposeful omission of details in the development of an abstract representation.
//	An important tool for managing complex systems.

//	An OO-Program is a community of objects that must interact to achieve their common goal.
//	Related classes are combined into namespaces. <(Namespaces are a scope management tool)>.


//	OOP and the Client-Server Relationship:
//	Server: provider of a service
//	Client: receiver of a service
//	<(The client and the server have different views of their relationship, since they will belong to different layers of abstraction)>
//	The definitions of the public methods of a class are its interface, and they form the level of abstraction its clients will deal with. 
//	The implementation of those methods constitutes a different, <(lower)> level of abstraction, that of the server.
//	Good OO-design separates both the design and implementation of client and server objects.

//	Software development is a matter of managing levels of abstraction. Software is a stack of levels of abstraction, each of which is vitally important, since the failure of any layer can break the stack.
//	A critical decision is finding the right levels of abstraction. A common error is to dwell on the lower levels, and neglecting to keep higher level structures independent.

//	Types of Abstraction:
//			Specialisation
//					Class Hierarchies
//			Division into Parts
//					Service View
//							ADT
//							Patterns
//							OOP
//					Repetition
//							Mathematical induction
//							Recursive algorithms
//							Recursive data structures
//							Composition
//					Catalogs
//							Cross references
//							Dictionaries
//			Multiple Views


//	Layers of Specialization: 'is-a' Class (Inheritance) Hierarchy
//	Transport
//			Wheeled
//					Car
//					Bus
//					Truck
//			Animal
//					Horse
//					Donkey
//			Aircraft
//					Fixed Wing
//					Rotary

//	Divide and Conquer: 'has-a' (Composition) divide a system into its constituent parts.
//	It is important to use the correct level of abstraction at each level, with each subsiquent level providing a finer level of detail than the previous.
//	Car
//			Engine
//					Block
//					Pistons
//					Valves
//			Fuel
//					Tank
//					Pump
//					Lines
//			Gearbox
//					Housing
//					Gears
//					Shifter
//			Body
//					Frame
//					Interior
//					Seats

//	


int main()
{
	return 0;
}

