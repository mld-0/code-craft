//	VIM SETTINGS: {{{3
//	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
//	vim: set foldlevel=2 foldcolumn=2:
//	{{{2
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	return 0;
}

//	Summary:
//	Error handling is a necessity, but if it obscures logic, it is implemented incorrectly (recall, a function should do one thing - error handling is one thing)
//	Use exceptions rather than return codes
//	Write try-catch-finally statement first
//	Use unchecked exceptions (don't specify exceptions in function signatures)
//	Exceptions should provide a message with context
//	Define exception class in terms of a caller's needs - create categories of exceptions where appropriate
//	Define the normal flow (encapsulate special case behaviour instead of using exceptions where possible)
//	Don't return null
//	Don't pass null

