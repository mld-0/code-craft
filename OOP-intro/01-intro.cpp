//	VIM SETTINGS: {{{3
//	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
//	vim: set foldlevel=2 foldcolumn=2:
//	}}}1
#include <iostream>
#include <vector>
#include <string>
using namespace std;
//	{{{2
//	Ongoings:
//	{{{
//	Ongoing: 2022-05-31T01:08:31AEST seeing the 'hierarchy of class implementation' (pre-perquisite classes for a class) where inheritance is not used (nicely listing them all in one place when using composition rather than inheritance) [...] (and inheritance vs composition (generally) re: said example)
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
//	O(M * N**2):
//	     DO 10 I = 1, N-M
//	      DO 10 J = 1, N-M
//	      FOUND = .TRUE.
//	      DO 20 K = 1, M
//	  20  IF X[I+K-1] .NE. X[J+K-1] THEN FOUND = .FALSE.
//	      IF FOUND THEN ...
//	10 CONTINUE
//	}}}
//	vs
//	{{{
//	O(M*N*ln(N))
//		APL, matrix of N rows / M columns, sort by rows, check for duplicate rows
//	}}}

//	Church's conjecture: any computation for which there is an efficient procedure can be realized by a Turing Machine
//	Sapir-Whorf hypothesis: it may be possible for an individual working in one language to utter ideas that cannot be translated (or even understood) by individuals working in another <linguistic-framework>.
//	<(A question of ideas vs implementation?)>
//	The choice of language will *direct* thoughts, but it cannot *proscribe* (inhibit/prevent) thoughts
//	}}}

//	An object will normally carry out an action by delegating-to/calling-on other objects. 
//	This is a natural fit for the kind of re-use that needed for modern software development.
//	A key aspect of OO-programs is information hiding - objects make an interface available to callers and keep their implementation hidden.

//	Example: hierarchy of class implementation
//		RobinFlorist: DeliveryPerson, FlowerAranger, Wholesaler
//			DeliveryPerson: Robin
//				Robin: Person
//			Wholesaler: Grower
//				Grower: Gardeners


//	Agents and communities:
//	OO-programs are structured around a community of objects interacting by making requests.
//			Agent: an object
//			Action: initiated through transmission of message to 'agent' (object) responsible for action.
//			Message: a request for a method, accompanied by additional information needed to carry out request
//			(Designated) Receiver: accepts responsibility for message, carries out the requested action
//			Method: responsible for carrying out the requested action


//	Message vs Procedural call:
//	{{{
//	wat?
//		A message (calling the method of an object) has a designated receiver
//		The interpretation of the method is determined by the receiver, and may be different for different receivers.
//	<(the specific receiver of a message <is/will> <usually/often/sometimes?> not be known until runtime? (necessitating 'late-binding') (<when> using an interpreted language, or pointer) (this is a C++-centric description is it not?))>
//	}}}
//	A message (method call) has a designated receiver, whereas a procedure call does not.
//	The interpretation of the message is determined by the receiver (different classes can define different versions of the same function).
//	<(There is late-binding between the message (object method call) and the code invoked (vs early-binding for a procedure call))>


//	Responsibilities:
//		



int main()
{
	return 0;
}

