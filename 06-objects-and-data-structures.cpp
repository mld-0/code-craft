//	VIM SETTINGS: {{{3
//	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
//	vim: set foldlevel=2 foldcolumn=2:
//	}}}1
#include <iostream>
#include <vector>
#include <string>
using namespace std;
//	{{{2

//	TODO: 2022-04-26T01:01:58AEST clean-code, 06-objects-and-data-structures, (actually implement 'shape' examples (since as we do so, we discover the problem slightly more than trivial), continue with other topics from chapter

//	Avoid blithely adding set/get/is methods. <(Seek to maximize encapsulation (where else (in effective-c++?) did 'encapsulation' come up?))>

//	Data Abstraction: Concrete vs Abstract Point
class PointConcrete {
public:
	//	implementation details are exposed to the world
	double x;
	double y;
};
class PointAbstract {
public:
	//	enforces access policy: coordinates can be read indervidually, but can only be set together
	double getX();
	double getY();
	void setCartesian(double x, double y);
	double getR();
	double getTheta();
	void setPolar(double r, double theta);
private:
	//	implementation details remain hidden from client
};


//	Hiding implementation is about abstractions. It exposes abstract interfaces that allow manipulation of the (essence of the) data. 
class VehicleConcrete {
public:
	double getFuelTankCapacityInGallons();
	double getGallonsOfGasoline();
};
class VehicleAbstract {
public:
	double getPercentFuelRemaining();
};
//	The second form exposes a more abstract form of our data. Where it is sufficent, it should be preferable.




//	Data/Object anti-symmetry
//	Objects hide their data behind abstractions, and expose functions that operate on that data.
//	Data-structures expose their data and have no meaningful functions.

//	Data Structure (Procedural)
struct PointDS {
	//	Ongoing: 2022-04-26T01:04:38AEST is <this> multiple-variable declaration not bad (and what is it called?)
	double x, y;
};
struct SquareDS {
	unique_ptr<PointDS> topLeft;
	double side;
};
struct RectangleDS {
	unique_ptr<PointDS> topLeft;
	double height;
	double width;
};
struct CircleDS {
	unique_ptr<PointDS> centre;
	double r;
};
//	'Geometry' provides the implementation
struct GeometryDS {
	double area(unique_ptr<SquareDS> shape);
	double area(unique_ptr<RectangleDS> shape);
	double area(unique_ptr<CircleDS> shape);
	//	Later addition of 'perimeter()' is possible without having to change Shape classes
};


class PointOO {
	double x;
	double y;
public:
	PointOO(double X, double Y) 
		: x(X), y(Y) {}
	//	Ongoing: 2022-04-26T00:59:16AEST best way to only accept initalizer list that must be 2 elements (presumedly <meaning/that-being>, how to reject anything else at compile time?)
	PointOO(initializer_list<double> init) {
		if (init.size() != 2) { throw invalid_argument("PointOO initializer_list must have size 2"); }
		x = init.begin()[0];
		y = init.begin()[1];
	}
};
class SquareOO {
	unique_ptr<PointOO> topLeft;
	double side;
public:
	double area() { return side * side; }
};
class RectangleOO {
	unique_ptr<PointOO> topLeft;
	double length;
	double width;
public:
	double area() { return length * width; }
};
class CircleOO {
	unique_ptr<PointOO> center;
	double r;
public:
	double area() { return 2 * 3.14159 * r; }
};
//	{{{
//	Ongoing: 2022-04-24T23:26:04AEST here we use <(template instantiation?)> (a compile time check) to ensure all types used with 'GeometryOO::area()' (support the interface) (which is defined by (how we use said type))
//	Ongoing: 2022-04-24T23:24:22AEST type deduction rules, vis-a-vis template classes vs template member functions
//	}}}
//	Parameterized type is used, allows use with any type supporting 'area()' (check is at compile type) [...] (but, using a template class prevents us from creating a single object instance to which any type can be passed (defeating the point))
struct GeometryOO {
	//	note: use of template member functions (not a template class)
	template<class T>
	double area(T* shape) { return shape->area(); }
	template<class T>
	double area_ii(unique_ptr<T> shape) { return shape->area(); }
	//	we cannot add 'perimeter()' without first implementing it for each shape class
};
//	{{{
//	Ongoing: 2022-04-24T23:29:58AEST Sort of defeats the point does it not? (use of template class results in an instance that can only be used for one of our shape types) (and having to move a unique pointer (and then the *nightmare* of having to return it again) (atomic that?))
//GeometryOO<typeof(c1)> g2;
//g2.area(pc1);
//g2.area(move(pc1));
//g2.area(pc1.get());
//	}}}



//	Ongoing: 2022-04-24T23:31:17AEST topics/questions raised within: (presumedly the correct way to pass a smart pointer is using the underlying raw pointer?) (the point of a smart pointer is ownership?) (virtual-functions/polymorphism and smart pointers?)
//	{{{
//	Ongoing: 2022-04-26T01:07:45AEST does [Shape]OO_i example offer anything (that is, is it worth implementing?)
//	Moar ramblings: extract the better-practice example
//	Ongoing: 2022-04-24T01:29:44AEST Whether (and once deciding it is), and why inheritance is necessary? [...] we don't have to, but we cannot add new classes later (throwing away an advantage of this method) without manually expanding 'Geometry', throwing away any advantage) [...] (the question: neccessary (seemingly no), preferable(?)) <- this question asked another way(?) do we want to shift work to run-time? [...] Does Effective-C++ have anything to say on when/whether to use virtual functions?
//	Ongoing: 2022-04-24T02:10:53AEST does public/private inheritance matter for inhertiance (other use/purpouse <examined> here?)
//	Problem example: (discussed elsewhere) (use 
class SquareOO_i {
	unique_ptr<PointOO> topLeft;
	double side;
public:
	double area();
};
class RectangleOO_i {
	unique_ptr<PointOO> topLeft;
	double side;
public:
	double area();
};
class CircleOO_i {
	unique_ptr<PointOO> center;
	double r;
public:
	double area();
};
//	Parameterized type is used, allows use with any type supporting 'area()' (check is at compile type)
template<class T>
struct GeometryOO_i {
	double area_ii(unique_ptr<T> shape) { return shape->area(); }
	//	we cannot add 'perimeter()' without first implementing it in each shape class
};
//	Ongoing: 2022-04-24T01:38:51AEST (is it?) preferable to declare virtual functions in derived class 'virtual' (is there not an effective-c++ lessson about this?) [...] '12-declare-overriding-funcs-override' [...] -> Only virtual member functions can be marked 'override' -> <and when it is, it must be implemented?> [...] -> 'override' forces one to include 'virtual' (and could that be half the point?)
//	<(and now doing it the other way)>
//	Ongoing: 2022-04-24T01:43:55AEST Is it (ever) acceptable to derive a class/struct, without explicitly specifying 'public/private' inheritance, (never-mind/especially-because the f---- of mixing class/struct pairs)?
//	Ongoing: 2022-04-24T01:45:10AEST public/private inheritance models -> (can you say?) is-a vs has-a (no -> that would be public inheritance vs containing-an-instance-of, or actually yes -> both those things are the latter -> would containing-an-instance-of be the preferable of the two?)
//	Can't create instances of an Abstract Base Class (which is (exactly)?)
//	Ongoing: 2022-04-24T02:06:58AEST (is it ever acceptable) and/or (does C++ allow one to) specify as an 'interface' (base class with pure virtual functions (or does interface mean more than that (and in what context))), variables instead of methods? 
//	Ongoing: 2022-04-24T02:13:27AEST (requirements vis-a-vis the <visibility> of virtual/overrided methods?) [...] (and whether said question makes any sense?)
//	Ongoing: 2022-04-24T02:14:46AEST (consider this) what is the necessity <or possible-purposue> of providing the class 'Geometry' with method 'area' when implementation is provided by the Derived shape classes?
struct ShapeOO_ii {
	virtual ~ShapeOO_ii() = 0;
	virtual double area() = 0;
};
ShapeOO_ii::~ShapeOO_ii() = default;
class SquareOO_ii: public ShapeOO_ii {
	unique_ptr<PointOO> topLeft;
	double side;
public:
	SquareOO_ii(double l)
		: side(l) {}
	virtual double area() override;
};
class RectangleOO_ii: public ShapeOO_ii {
	unique_ptr<PointOO> topLeft;
	double length;
	double width;
public:
	RectangleOO_ii(double l, double w)
		: length(l), width(w) {}
	virtual double area() override;
};
class CircleOO_ii: public ShapeOO_ii {
	//	Would 'PointOO center' not be better? (is there not no-point to using a smartpointer here?)
	unique_ptr<PointOO> center;
	double r;
public:
	//	Ongoing: 2022-04-26T01:00:53AEST now way to use 'make_unique' in an initalizer list (would it not be better to do so inside the ctor body) (or just not to f----- use smartpointers in this way in the first place?)
	//	TODO: 2022-04-26T00:53:45AEST (what is better practice), taking (double, double, double) or (Point, double)? (and it would be best if one could pass '{double,double}, double'
	CircleOO_ii(PointOO c, double R)
		: center(new PointOO(c)), r(R) {}
	virtual double area() override;
};
//	(observation:) 'GeometryOO_ii' doesn't have to inherit anything(?) [...] it's purpouse is to demonstrate polymorphic use of 'ShapeOO_ii'?
struct GeometryOO_ii {
	//	Ongoing: 2022-04-24T02:18:16AEST can/should a raw pointer (or smart pointer) be used for this purpouse?
	double area_i(ShapeOO_ii* shape) { return shape->area(); }
	double area_ii(unique_ptr<ShapeOO_ii> shape) { return shape->area(); }
};
//	Ongoing: 2022-04-24T02:37:31AEST in all this f----- around, the point was missed that one doesn't pass 'unique_ptr' without transfering ownership (so.... what <you> are saying is that raw pointers (to the base class?) for the 'GeometryOO' function (or just using 'T' -> not solving our instantitation problem) [...] (this being (another) place to leave things?)
//	}}}

int main()
{
	CircleOO c1;
	unique_ptr<CircleOO> pc1( new CircleOO() );

	//	Ongoing: 2022-04-24T02:34:57AEST (oh no), (being a place to leave things) -> usage of 'GeometryOO<>::area()'? -> this 

	//GeometryOO g1;
	//g1.area(c1);

	return 0;
}


