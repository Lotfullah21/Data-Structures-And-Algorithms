## Recursion

the idea of taking a problem and reducing it into smaller problems.
in programming language, it is a technique that a function call itself again and again.

to avoid infinite recursion, we need to have one or more base case which causes the function to stop calling itself after reaching to those base cases.

for instance, using for or while loops make our process iterative process. in this case we are capturing computation in a set of state variables.
at each iteration these state variables will get updated.

### Some Important points to be remembered. (AlgoPrep)

##### follow 3 steps

### 1. Faith:

define what your function should do and have faith it works.

### 2. Main Logic:

solve the problem with subproblem.

### 3. Base Case:

Solution to smallest sub problem.

### Few other Important points to be remembered.

1. whenever there is a call on a function a brand new local scope for that function will be created in memory.

2. the value of that function will be returned to the previous function that created this function.

3. variable across local scopes are not connected, which means if you change something in fn_3, it will not be reflected in fn_2.
4. each variable is a different object in different even if they are having same names.
5. No value will be returned until you touch the base case.

6. after base case, the flow is backward.
