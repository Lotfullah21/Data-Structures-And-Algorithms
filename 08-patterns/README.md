# Patterns

1. First and foremost, identify the pattern, do not worry about the kind of elements there, think if you can just can print that pattern with zeros.
2. number of lines == number of rows == number of times the outer loop runs.
3. Identify for every row how many columns are there, what are the types of elements and how the columns are changing in relation to the rows.
4. Identify what do you need to print.

### Note:

`py range()` function starts from `0` if we do not specify starting point.

in other languages like JavaScript a loop looks like this `for (var i=1; i<=n; i++)` but in python it will not be `for i in range(1, n)`, because here n is excluded,
it should be `for i in range(1, n+1)`
