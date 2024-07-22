Use array to keep the count, because across functions, changes are reflected in the arrays.



The ans variable is a list initialized to [0] and passed to the helper method.
Any updates to ans inside the helper method will affect the same list, ensuring the count of subsets summing to k is accurate.
The final result is obtained by accessing ans[0].
