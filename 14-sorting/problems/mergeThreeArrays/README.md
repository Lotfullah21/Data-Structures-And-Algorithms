### Question:

Given three sorted arrays A, B and C of size N, M and P respectively. The task is to merge them into a single array which must be sorted in increasing order.

Input: A = [1, 2, 3, 4]
B = [1, 2, 3, 4, 5]
C = [1, 2, 3, 4, 5, 6]
result = solution.mergeThree(A, B, C)
print(result)

Output: [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]

### Idea:

Keep three pointers and

- Use or in the while loop to ensure that the loop continues until at least one of the pointers reaches the end of its array.
- After finding the min-value among all at each iteration, increment the pointer related to the array which min-value was found.

### Analysis:

`Time Complexity`: O(N + M + P)
`Auxiliary Space`: O(N + M + P) for the resultant array only.

### Learned:

The earlier `if` statements update minVal independently, potentially modifying it multiple times.
The later `if-elif` statements are mutually exclusive, executing only the first condition that is met and incrementing the corresponding pointer.
This distinction in behavior ensures that minVal correctly holds the minimum value among the elements being compared, and the pointers `i`, `j`, and `k` are advanced appropriately after each iteration through the loop.
