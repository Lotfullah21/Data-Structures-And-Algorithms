### Question:

Given an unsorted array of positive integers, find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any of the two values (or sides) must be greater than the third value (or third side)

### Analysis:

`Time complexity`:`O(n^2)`, where n is the number of elements in the array. This is because we have three nested loops, but the innermost loop (k) is not executed for every i and j, as it is incrementing from the previous value.
