factorial(4) = 1 _ 2 _ 3 _ 4
factorial(5) = 1 _ 2 _ 3 _ 4 _ 5
factorial(5) = 5 _ factorial(4) => n \* factorial(n - 1)
base case: if n ==1: return and do not call another function.
after reaching the base case, the flow will be in reverse direction.
 