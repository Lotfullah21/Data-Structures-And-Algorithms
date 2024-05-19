### Base Case:

base case in a recursive call is the situation where the function can be called any more.
Either the function call should stop and return nothing or based on our problem, it needs to return some values.

if the base case is not handled, in python all function calls are stored in stack memory and when a function calls itself many times that memory will be filled and it returns maximum calls reached.

