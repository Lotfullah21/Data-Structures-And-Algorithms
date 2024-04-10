### Anagram

Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not.
An anagram of a string is another string that contains the:

- same characters,
- number of times each character appears should be the same in other string.

### Idea-1:

Sort both of the strings, after sorting if they are matched, then they are anagram of each other.

#### Analysis:

`Time Complexity`: `O(NlogN)`, for sorting algorithm.

### Idea-2:

Maintain a count array.

- add to the count of s1 +1
- add to the count of s2 -1
  After finishing the loop, still count is not zero, it means there was some number that was not present in s1, so they are not anagram of each other.

#### Analysis:

`Time Complexity`: `O(N)`, N is length of the string.
