//	VIM SETTINGS: {{{3
//	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
//	vim: set foldlevel=2 foldcolumn=2:
//	}}}1
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
//	{{{2
//	TODO: 2022-05-18T02:12:01AEST code-craft/clean-code/03-functions, plausible data-flow / roles for each object, complete example doing something that makes calls of 'renderPageWithSetupsAndTeardowns' make sense

//	Functions implement subroutines in modern languages. 
//	They are the first line of organization in any program.

//	Classes for renderPageWithSetupsAndTeardowns example
struct StringBuffer {
	vector<string> buffer;
	void append(const string& content) { buffer.push_back(content); }
	//	Ongoings:
	//	{{{
	//	Ongoing: 2022-05-18T00:51:06AEST 'to_string_i()' (is it faster to pop_back final newline than it is to check each loop iteration whether/not to insert it?) 
	//	Ongoing: 2022-05-18T00:53:34AEST use only 1 return statement (allows copy-elision) (and better practice anyway) 
	//	Ongoing: 2022-05-18T00:36:46AEST see C++-examples/bench-join-vector-strings for various implementations of join vector<string>
	//	}}}
	string to_string() {
		//	{{{
		stringstream ss;
		auto l = [&ss, delim="\n"](const string& x) { ss.eof() ? ss << delim << x : ss << x; };
		for_each(buffer.begin(), buffer.end(), l);
		return ss.str();
	}
	//	}}}
};
struct WikiPage {
	//string text;
	//WikiPage(const string& t) 
	//	: text(t) 
	//{}
};
class PageData {
	string content = "Lorem Ipsum";
	string title = "PageData Example Title";
	vector<string> conf;
public:
	void addAttribute(string category) { if (hasAttribute(category)) { return; } conf.push_back(category); }
	void setContent(string content_new) { content = content_new; }
	bool hasAttribute(string category) const { return find(conf.begin(), conf.end(), category) != conf.end(); }
	string getTitle() const { return title; }
	string getContent() const { return content; }
	WikiPage getWikiPage() const { return WikiPage(); }
	string getHtml() const { return "<title>" + getTitle() + "</title>\n<body>" + getContent() + "</body>"; }
};

//	Functions for renderPageWithSetupsAndTeardowns example
void includeSetupPages(WikiPage& testPage, StringBuffer& newPageContent, bool isSuite) {
}
void includeTeardownPages(WikiPage& page, StringBuffer& content, bool isSuite) {
}

//	Book example, <fixed> function: renderPageWithSetupsAndTeardowns
//	<(Done by method extracting / renaming / restructuring first horror-show example)>
string renderPageWithSetupsAndTeardowns(PageData& pageData, bool isSuite) {
	bool isTestPage = pageData.hasAttribute("test");
	if (isTestPage) {
		//	<contents?> from PageData 
		WikiPage testPage = pageData.getWikiPage();
		//	<vector of strings>
		StringBuffer newPageContent;
		//	<(putting stuff (settings?) from pageData -> testPage -> newPageContent)>
		includeSetupPages(testPage, newPageContent, isSuite);
		//	putting pageData.contents -> newPageContent
		newPageContent.append(pageData.getContent());
		//	<(putting(?) )>
		includeTeardownPages(testPage, newPageContent, isSuite);
		//	newPageContent -> pageData
		pageData.setContent(newPageContent.to_string());
	}
	return pageData.getHtml();
}
//	A function should do one thing: this function is doing 3: 
//			1) determine whether 'pageData' is a test page
//			2) if so, include setups/teardowns
//			3) render the page in html



//	Shortened again:
bool isTestPage(const PageData& pageData) {
	return pageData.hasAttribute("test");
}
void includeSetupAndTeardownPages(PageData& pageData, bool isSuite) {
	//	<(here goes contents of if-statement from 'renderPageWithSetupsAndTeardowns'? (when we decipher it))>
	//	{{{
	//	<contents?> from PageData 
	WikiPage testPage = pageData.getWikiPage();
	//	<vector of strings>
	StringBuffer newPageContent;
	//	<(putting stuff (settings?) from pageData -> testPage -> newPageContent)>
	includeSetupPages(testPage, newPageContent, isSuite);
	//	putting pageData.contents -> newPageContent
	newPageContent.append(pageData.getContent());
	//	<(putting(?) )>
	includeTeardownPages(testPage, newPageContent, isSuite);
	//	newPageContent -> pageData
	pageData.setContent(newPageContent.to_string());
	//	}}}
}
string renderPageWithSetupsAndTeardowns_ii(PageData& pageData, bool isSuite) {
	if (isTestPage(pageData)) {
		includeSetupAndTeardownPages(pageData, isSuite);
	}
	return pageData.getHtml();
}
//	Ongoing: 2022-05-18T03:08:47AEST a hierachy to functions (namespaces? classes?), beyond simply having function explosion at global scope (how would one do it for book examples?) (see above)


//	Rule 1: Small
//	The first rule of functions is that they should be small. (The second rules is they should be even smaller than that).
//	This implies that blocks within if/else/for/while statements should be one line long (probably a function call).
//	This adds documentary value, because every block gets a descriptive name.
//	Limit nested structures. Ideally >= 2 levels.


//	Rule 2: Do One Thing
//	Functions should do one thing. They should do it well. They should do it only. The purpouse of a function is to decompose a larger concept (described by function name) into steps at the next level of abstraction.
//	If a function does only those steps that are one level below the stated name of the function, then the function is doing only one thing. Or: 
//	<(If one can extract another function with a name that is not merely a restatement of the containing functions implementation, that function is doing more than one thing.)>
//	<(Functions that do one thing cannot be reasonably divided into sections)>


//	Rule 3: One level of abstraction per function
//	<>


//	Rule 4: The stepdown rule
//	<>


//	Rule 5: Descriptive names
//	<>


//	(Alternatives to switch statement: the AbstractFactory)
//	<>


//	Function Arguments:
//	<>


//	Have No Side Effects:
//	<>

//	Output Arguments:
//	<>


//	Command Query Seperation:
//	<>


//	Prefer Exceptions to Error Codes:
//	<>


//	Extract Try/Catch Blocks:
//	<>


//	Error handling is One Thing:
//	<>


//	Don't Repeat Yourself:
//	<>


//	Structured Programming:
//	<>


//	How To Approach Writing Functions:
//	<>


//	Other Examples:
//	Continue: 2022-05-18T02:15:22AEST functions theory, implementation(/better-examples) can come later [...] (another reference for 'what makes a good function' (something online, with better examples to draw from?))

//	LINK: https://en.wikipedia.org/wiki/SOLID
//	{{{
//	}}}

//	LINK: https://dev.to/levivm/coding-best-practices-chapter-one-functions-4n15
//	{{{
//	}}}

//	LINK: https://www.quora.com/What-are-some-best-practices-in-defining-function-or-method-parameters-in-programs
//	{{{
//	}}}

//	LINK: https://www.reddit.com/r/coding/comments/9yfv4/best_practice_should_functions_return_null_or_an/
//	{{{
//	}}}

int main()
{
	vector<string> vs1 = { "abc", "def", "hij", "klm", "nop", "qrs", "tuv", "wxyz" };
	StringBuffer sb1;
	sb1.buffer = vs1;
	cout << "sb1.to_string_i()=(" << sb1.to_string() << ")\n";

	return 0;
}

