### Question:

Given N elements, Rearrange the array so that

a) arr[0] should go to correct sorted position
b) all elements <=arr[0] should go to left side of arr[0]
c) all elements >arr[0] should go to right side of arr[0]

after moving the elements to the left and right side of the target, the elements should be sorted necessarily.

Input: [6, 2, 3, 1, 12,9, 0,11]
target = 16
Output: [2, 3, 1, 0, 6, 12, 9, 11]

Explanation: all element smaller than `6` are on the left hand side and larger than `6` are on the right hand side.

### Idea-1:

Sort the array, all elements smaller than target will move to the left and larger elements to the right.

`Time complexity`: `O(NlogN)`, because of using sort method.
`Space Complexity`: `O(1)`, No extra space used.

### Idea-2:

#### Steps

- keep two pointers.
- p1 for elements smaller than arr[s].
- p2 for elements greater than arr[s].
- check if arr[p1] is smaller than arr[s].
- if true, increment the p1.
- check if the arr[p2] is greater than arr[s].
- if true, decrement the p2.
- if none of the condition is true
  - swap p1 and p2
  - increment and decrement p1 and p2.
- swap the 0th index with p2.

Use two pointers
