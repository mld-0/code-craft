#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2

#   Ongoings:
#   {{{
#   2023-08-18T21:09:03AEST what about `assert [ True, True, False, False ] == get_HW_HBCA_States(hw)` as a solution to the 'One Assert per Test' problem?
#   2023-08-18T21:18:22AEST single concept per test -> (to what extent does that mean/not-mean single testcase per test?)
#   }}}

#   Unit Tests:
#       Demonstrate and validate the correctness of new code
#       Make it vastly easier and safer to modify and improve existing code


#   Write tests and production code together:
#       First, write a test which describes a specific requirement of the production code
#       Second, write no more production code than is necessary to satisfy that test
#   This cycle should be short.
#   If all code is written this way, then virtually all code will be covered by tests.
#   Don't count on adding tests later, recall: later = never.


#   Apply the same quality standards to tests as to production code.
#   A good test is a readable test. Try to hide unnecessary details
#   Structure of a test: Build, Operate, Check

#   Tests should run quickly. Tests should be run often. 
#   Tests that take too long will not be run often enough.


#   Domain-specific testing language:
#   <>


#   Minimise Assertions per Test (ideally, to only one)
#   Contention:
#           assert "HBca" == hw.getState()
#   Is quicker and easier to read than
#           assert True  == hw.heaterState()
#           assert True  == hw.blowerState()
#           assert False == hw.coolerState()
#           assert False == hw.alarmState()
#   Especially where we are going to be testing lots of combinations of these things


#   Single Concept per Test:
#   Each test should be of one specific behaviour. 
#   Create different tests for each different behaviour of a function.
#   <>


#   Tests should be FIRST:
#       - Fast
#       - Independent of each other
#       - Repeatable in any environment
#       - Self-validating (not require the user to investigate whether they have passed)
#       - Timely (written together with the code they test)

