### Question

Given a sorted array with N elements and 3 indices start, mod and end such that subArray [s,m] is sorted, subArray [m+1,e] is sorted. Sort the subArray from start to end index [s,e].

Note: end always does not till the end of the array, it can be up to some point greater than mid+ 1. start to mid and then mid+1 to end are continuous subArray.

#### Idea

Use the though process behind selection sort, where the pointers are starting from given start end and mid+1 index.

#### Note:

The given array should be a random array.
It should have the following features:

- from `start-mid` sub-array is sorted
- from `mid+1-end` sub-array is sorted

### Analysis

`Time complexity`: `O(N^2)`.
`Space Complexity`: `O(1)`.
