//	VIM SETTINGS: {{{3
//	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
//	vim: set foldlevel=2 foldcolumn=2:
//	}}}1
#include <iostream>
#include <vector>
#include <array>
#include <string>
using namespace std;
//	{{{2
constexpr double pi = 3.141592653589793238463;
//	Ongoings:
//	{{{
//	Ongoing: 2022-04-26T00:59:16AEST 'Point' best way to only accept initalizer list that must be 2 elements (presumedly <meaning/that-being>, how to reject anything else at compile time?)
//	Ongoing: 2022-06-14T01:44:02AEST What C++/compiler version is required to use 'array<T,len>' instead of initalizer_list<T> (as a way to enforce size=len)?
//	Ongoing: 2022-04-24T23:26:04AEST GeometryOO, here we use <(template instantiation?)> (a compile time check) to ensure all types used with 'GeometryOO::area()' (support the interface) (which is defined by (how we use said type))
//	Ongoing: 2022-04-24T23:24:22AEST GeometryOO, type deduction rules, vis-a-vis template classes vs template member functions
//	Ongoing: 2022-05-08T21:19:59AEST GeometryOO, (whether templates/inheritance are a better choice, the lesson of OO/DS anti-symmetry is applicable to both?)
//	Ongoing: 2022-05-08T20:53:11AEST GeometryOO, does 'polymorphic' describe use of template functions (or does it <imply/require> inheritance/virtual-functions)?
//	Ongoing: 2022-05-08T20:40:39AEST GeometryOO, C++, best practices, using templates for 'GeometryOO' (vs using inheritance/virtual-functions)?
//	Ongoing: 2022-04-24T23:29:58AEST GeometryOO, Sort of defeats the point does it not? (use of template class results in an instance that can only be used for one of our shape types) (and having to move a unique pointer (and then the *nightmare* of having to return it again) (atomic that?))
//	Ongoing: 2022-05-08T21:53:49AEST 'law of demeter' (but in an intuitive/easy-to-understand form)
//	}}}

//	TODO: 2022-04-26T01:01:58AEST clean-code, 06-objects-and-data-structures, (actually implement 'shape' examples (since as we do so, we discover the problem slightly more than trivial), continue with other topics from chapter
//	TODO: 2022-04-26T00:53:45AEST 'CircleOO_ii, (what is better practice), taking (double, double, double) or (Point, double)? (and it would be best if one could pass '{double,double}, double'
//	TODO: 2022-05-08T22:13:05AEST clean-code, 06-objects-and-data-structures, (what is the better solution to a design failure like) 'ctxt.getOptions().getScratchDir().getAbsolutePath()'?


//	Hiding implementation by offering abstract interfaces that allow manipulation of the essence of the data.

//	Data Structure:
//	implementation details are exposed to the world
class PointConcrete {
public:
	double x;
	double y;
};

//	Object:
//	methods enforces access policy: coordinates can be read indervidually, but can only be set together
//	implementation details remain hidden from client
class PointAbstract {
public:
	double getX();
	double getY();
	void setCartesian(double x, double y);
	double getR();
	double getTheta();
	void setPolar(double r, double theta);
private:
};


//	Encapsualation: 
//	<>

//	Example: This second form exposes a more abstract form of our data. Where it is sufficent, it should be preferable.
class VehicleConcrete {
public:
	double getFuelTankCapacityInGallons();
	double getGallonsOfGasoline();
};
class VehicleAbstract {
public:
	double getPercentFuelRemaining();
};
//	Avoid blithely adding set/get/is methods, instead seek to maximize encapsulation.



class Point {
	double x, y;
public:
	Point(double X, double Y) : x(X), y(Y) {}
	Point(std::array<double,2> vals) : Point(vals[0], vals[1]) {}
	Point(Point&) = default;
	double getX() { return x; }
	double getY() { return y; }
};

//	Data/Object anti-symmetry
//	Objects hide their data behind abstractions, and expose functions that operate on that data.
//	Data-structures expose their data and have no meaningful functions, <leading to> procedural <code/implementations>
//	'Everything-is-an-object' is a myth. Sometimes, the best choice is simple data structures operated on by procedures.


//	Data-Structure: 
//	Hard to add classes, easy to add functions.
struct RectangleDS {
	Point topLeft;
	double height, width;
};
struct CircleDS {
	Point center;
	double r;
};
//	must implement 'area()' for each supported type
//	Can implement 'perimeter()' without having to change each classes
struct GeometryDS {
	double area(const RectangleDS& shape) { return shape.height * shape.width; }
	double area(const CircleDS& shape) { return 2 * pi * shape.r; }
};


//	Object-oriented implementation
//	A class should hide its internal data structure, and expose operations. 
//	Easy to add classes, hard to add functions.
class RectangleOO {
	Point topLeft;
	double length, width;
public:
	RectangleOO(Point tl, double l, double w) : topLeft(tl), length(l), width(w) {}
	RectangleOO(RectangleOO&) = default;
	double area() { return length * width; }
};
class CircleOO {
	Point center;
	double r;
public:
	CircleOO(Point Center, double R) : center(Center), r(R) {}
	CircleOO(CircleOO&) = default;
	double area() { return 2 * pi * r; }
};
//	implementation of 'area()' is provided by each class
//	Cannot add 'perimeter()' without first changing each class
struct GeometryOO {
	template<class T>
	double area(T& shape) { return shape.area(); }
	template<class T>
	double area(T* shape) { return shape->area(); }
	//	we cannot add 'perimeter()' without first implementing it for each shape class
};


//	Hybrids: classes that are partial Objects and partially Data-structures
//	(uses functions to perform significant tasks, but makes class variables accessible)
//	(Combines downsides of both data-structures and objects - hard to add new data, and hard to add new methods) 
//	indicative of a muddled design, avoid.


//	Law of Demeter: 
//	If A owns B, and B owns C, A should use B to manipulate C instead of trying to do so itself
//	A module should not know about the innards of the object it manipulates.
//	A method should only call the methods of objects passed to it as arguments, or that are fields of the class it belongs to
//	Don't talk to strangers: avoid method chaining (calling methods of objects returned by other methods)
//	{{{
//	A method 'f' of class 'Widget' whould only call these methods:
//		Methods belonging to 'Widget'
//		An object created <by/inside?> 'f'
//		An object passed as argument to 'f'
//		An object held in an instance variable of 'Widget'
//	(not methods of objects that are returned by any of these functions) (talk to friends, not strangers)
//	(common violation: 'train-wrecks') (whether example below violates Law of Demeter depends on whether ctxt/opts/scratchDir are objects (yes) or data-structures (no)).
//	}}}
//	Example: `Store` does not access methods/fields of `Wallet`, but instead only uses the interface provided by `Person`
class Wallet {
public:
	Wallet(int amount) : _amount(amount) {}
	bool debit(int amount) {
		if (_amount >= amount) {
			_amount -= amount;
			return true;
		}
		return false;
	}
	int get_balance() const { return _amount; }
private:
	int _amount;
};
class Person {
public:
	Person() : wallet(100) {}
	int show_balance() const { return wallet.get_balance(); }
	bool make_payment(int amount) { return wallet.debit(amount); }
private:
	Wallet wallet;
};
class Store {
public:
	string purchase(Person& person, int cost) {
		if (person.make_payment(cost)) {
			return "Purchased";
		} 
		return "Declined";
	}
};


//	Train-wreck: 
//	LINK: http://randomthoughtsonjavaprogramming.blogspot.com/2013/10/trainwreck-vs-method-chaining.html
///	A chain of methods with returned objects of different types
//			final String outputDir = ctxt.getOptions().getScratchDir().getAbsolutePath()
//	This Better written as:
//			Options opts = ctxt.getOptions();
//			File scratchDir = opts.getScratchDir();
//			final String outputDir = scratchDir.getAbsolutePath();
//
//	Fluent interface:
//			Person larry = (new Person()).setName("larry").setJob("Chief Mouser");
//	A chain of methods with returned objects of the same type does not break the law of demeter
//	(This can be an alternative to resorting to ctors with many arguments, although in this case an expression builder may be a better solution)
//
//	Expression-builder: 
//	A seperate class, which hides the underlying method-chaining to create an object, providing a single method for each combination of arguments


//	Hiding structure: (consider)
//			ctxt.getAbsolutePathOfScratchDir()
//	vs
//			ctxt.getScratchDir().getAbsolutePath()
//	The first approach is likely to lead to an explosion in the number of methods. <(The second presumes 'getScratchDir()' returns a data strucutre (instead of an object)?)>. (Both are unappealing options).
//	Instead: consider what the caller is likely trying to do: read a file in the scratch-dir
//	So, make `getAbsolutePathOfScratchDir()` a private method, and provide a public method `createScratchFileStream()` which handles creating/opening the file without requiring the caller to handle details like the path of the scratch-dir



//	Fluent-Interface: 
//	LINK: https://martinfowler.com/bliki/FluentInterface.html
//	[{Interface built on method chaining}]
//	{{{
//	}}}


//	Data-Transfer-Object: a class with public variables and no functions
//	Active-Record-Object: Hybrid form of data-transfer-object, provides navigational methods like 'save()' and 'find()' (bad: use a seperate object containing this logic)


//	LINK: https://medium.com/vattenfall-tech/the-oop-has-been-explained-wrongly-to-me-db8e36f91bb2
//	{{{
//	}}}


//	Resources:
//	<>


int main()
{
	//CircleOO c1;
	//unique_ptr<CircleOO> pc1( new CircleOO() );

	Point p1( {1,2} );
	CircleOO c2( {1,2}, 3 );

	GeometryOO g1;
	cout << "g1.area(coo2)=(" << g1.area(c2) << ")\n";

	return 0;
}

//	Summary:
//	Objects expose behaviour and hide data. This makes it easy to add new kinds of objects, but difficult to add new features/behaviour.
//	Data structures expose data and have no significant behaviour. This makes it easy to add new features/behaviour, but difficult to add new kinds of data-structures.
//	'Everything-is-an-object' is a myth, choose the best option for a given task.
//	If A owns B, and B owns C, A should use B to manipulate C instead of trying to do so itself
//		<>

