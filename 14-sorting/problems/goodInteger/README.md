### Question

Given an array of integers, find the good integers.
What is a good integer? A number is said to be a good integer if number of elements smaller than that number equals to the value of that number.

For instance if the a number is == 3 and number of smaller element than 3 is also 3, then 3 is a good integer.

Input: [1, -1, 2, 3,-2]
Output: 1
for integer 1, smaller elements are -1 and -2.

#### Idea-1:

For every integer, count number of integers smaller than that number and compare it with the value itself, if equal, return that number.

```py
def goodIntegers(arr: list) -> list[int]:
    "Returns number of good integers"
    n = len(arr)
    goodIntegers = []
    for i in range(n):
        c = 0
        for j in range(n):
            if arr[i]>arr[j]:
                c+=1
        if c==arr[i]:
            goodIntegers.append(arr[i])
    return goodIntegers

```

#### Analysis:

`Time Complexity`: `O(N^2)` because of the nested loop.
`Space complexity`: `O(1)`, no extra space is used.

### Idea-2:

after sorting, the numbers that are less than a number is the index number itself.

```py

def goodIntegers(arr: list) -> list[int]:
    n = len(arr)
    goodIntegers = []
    arr.sort()
    for i in range(n):
        if arr[i]==i:
            goodIntegers.append(arr[i])
    return goodIntegers
```

#### Analysis:

`Time Complexity`: `O(NlogN)` because of sorting the array.
`Space complexity`: `O(1)`, no extra space is used.

# Question-2:

### Good integers with repeated elements.

#### Idea-1:

same as previous question procedures.

#### Idea-2:

- If numbers are repeated, all occurrence of the same number is going to be either good or bad.
- If element is first occurrence, number of smaller element that the number is the index itself.

How to check for first occurrence:
compare `arr[i]` with `arr[i-1]`.

```py

def goodIntegers(arr: list) -> list[int]:
    "Returns number of good integers"
    n = len(arr)
    goodIntegers = []
    smallerNumbersCount = 0
    smallerGoodIntegerCounts = 0
    # Taking care of the edge case, at 0th, we will be 0 number that is smaller than the 0 itself.
    if arr[0]==0:
        smallerGoodIntegerCounts+=1
    for i in range(n):
        # Only update smallerCounts variable when the element is occurring for the first time.
        if arr[i]!=arr[i-1]:
            smallerNumbersCount = i
        # If not first occurrence, do nothing.
        else:
            pass
        # If current element has same value as smaller count, it is a good integer.
        if arr[i]==smallerNumbersCount:
            goodIntegers.append(arr[i])
            smallerGoodIntegerCounts +=1
    return goodIntegers, smallerGoodIntegerCounts
```

#### Analysis:

`Time Complexity`: `O(NlogN)` because of sorting the array.
`Space complexity`: `O(1)`, no extra space is used.
