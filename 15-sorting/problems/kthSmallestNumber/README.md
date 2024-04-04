### Question:

Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Input: [0,4, 5, 3, 1]
k = 2
Output: 1
Explanation: the 2nd largest element in the above array is 1.

### Idea-1:

Sort the array and return k-1th element. Why k-1th? because array is 0th based.
