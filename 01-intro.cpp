//	VIM SETTINGS: {{{3
//	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
//	vim: set foldlevel=2 foldcolumn=2:
//	}}}1
#include <iostream>
#include <vector>
#include <string>
using namespace std;
//	{{{2

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

//	Example: DNA sequence as a vector of N integers, discover whether any pattern of length M is ever repeated.
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


//	Agents and communities:
//	An object-oriented program is structured around A community of objects interacting by making requests.
//			agent: an object
//			message: <(argument? other methods of passing information to an object)>
//			method: <(implementation, details of which are typically hidden from caller (and may involve delegations to other classes in the hierarchy of the <problem/solution-space>?))>
//	{{{
//	Example: classes used to implement each class
//		RobinFlorist: DeliveryPerson, FlowerAranger, Wholsaler
//				DeliveryPerson: Robin
//				Wholesaler: Grower
//						Grower: Gardeners
//	}}}

//	Message and methods
//		Action is initiated through transmission of message to 'agent' (object) responsible for action.
//		Message encodes request for action, is accompanied by additional information needed to carry out request
//		Message is sent to 'receiver', who accepts responsibility and carries out the action.
//		An object will normally carry out an action by delegating to other objects. This <supports/is-conducive> to the kind of software re-use that is a vital to modern software development.


//	Message vs Procedural call:
//		A message (calling the method of an object) has a designated receiver
//		The interpretation of the method is determined by the receiver, and may be different for different receivers.
//	<(the specific receiver of a message <is/will> <usually/often/sometimes?> not be known until runtime? (necessitating 'late-binding') (<when> using an interpreted language, or pointer) (this is a C++-centric is it not?))>


//	Responsibilities:



int main()
{
	return 0;
}

