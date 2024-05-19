### Count Sort Algorithm

##### step-1:

Find out the maximum element in the array.

```py
maxElement = -inf
for i in range(0, len(arr)):
    currentMax = max(arr[i], maxElement)
```

##### step-2:

Generate an array of size `currentMax` of original array and fill it with the frequency or occurrence of each element in the original array.

```py
n = len(arr)
count = [[] for _ in range(currentMax)+1]
for i in range(n):
    val = arr[i]
    count[val] = count[val] + 1

# Dry Run

Lets say the array is [0, 3, 1, 1, 0, 4, 6, 7, 3, 1]
max = 7
# Generate an empty array of size max:
arr = [0, 3, 1, 1, 0, 4, 6, 2, 3, 1]
count = [0, 0, 0, 0, 0, 0, 0, 0]

i = 0;
val = arr[0] = 0;
count[0] = 0 + 1;
count = [1, 0, 0, 0, 0, 0, 0, 0];

i = 1;
val = arr[i] = arr[1] = 3;
count[3] = 0 + 1  = 1;
count = [1, 0, 0, 1, 0, 0, 0, 0];

i = 2
val = arr[i] = arr[2] = 1
count[1] = 0 + 1
count = [1, 1, 0, 1, 0, 0, 0, 0];

i = 3
val = arr[i] = arr[3] = 1
count[1] = 1 + 1 = 2
count = [2, 1, 0, 1, 0, 0, 0, 0];

i = 4
val = arr[i] = arr[4] = 0
count[0] = 1 + 1 = 2
count = [2, 2, 0, 1, 0, 0, 0, 0];

i = 5
val = arr[i] = arr[5] = 4
count[0] = 0 + 1 = 1
count = [2, 2, 0, 1, 1, 0, 0, 0];

i = 6
val = arr[i] = arr[6] = 6
count[0] = 0 + 1
count = [2, 2, 0, 1, 1, 0, 1, 0];

i = 7
val = arr[i] = arr[7] = 7
count[7] = 0 + 1
count = [2, 2, 0, 1, 1, 0, 1, 1];

```

#### Step-3:

Do the sorting, go through original array and found its occurrence in count array, based on count array, replace the original array with the numbers in count array based on their frequency.

```py
k = 0
for i in range(0, max+1):
    c = count[i]
    for _ in range(0, c):
        arr[k] = i
        k+=1

outer-loop = range(0, max+1) = range(8)
i = 0;
c = count[0] = 2;
range = range(0, 2)
arr[k] = i => arr[0] = 0; k+=1 => 0+1=1;
arr[k] = i => arr[1] = 0; k+=1 => 1+1=2;
first k: [0, 3, 1, 1, 0, 4, 6, 7, 3, 1]
second k: [0, 0, 1, 1, 0, 4, 6, 7, 3, 1]



i=1
c = count[i] = count[1] = 2
range = range(0, 2)
arr[k] = i => arr[2] = 1; k+=1 => 2+1=3;
arr[k] = i => arr[3] = 1; k+=1 => 3+1=4;
first k: [0, 0, 1, 1, 0, 4, 6, 7, 3, 1]
second k: [0, 0, 1, 1, 0, 4, 6, 7, 3, 1]


i = 2
c = count[i] = count[2] = 0; range(0);
Not Entering the loop;

i = 3
c = count[i] = count[3] = 1;
range = range(0, 1)
arr[k] = i => arr[4] = 3; k+=1 = 4+1=5
arr = [0, 0, 1, 1, 3, 4, 6, 7, 3, 1]

i=4
c = count[i] = count[4] = 1;
range() = range(0, 1)
arr[k] = i => arr[5] = 5; k+=1 = 5+1=6
arr = [0, 0, 1, 1, 3, 5, 6, 7, 3, 1]

i=5
c = count[2] = 0; range(0);
Not Entering the loop;
arr = [0, 0, 1, 1, 3, 5, 6, 7, 3, 1]


i = 6
c = count[i] = count[6] = 1;
range() = range(0, 1)
arr[k] = i => arr[5] = 6; k+=1 = 5+1=7
arr = [0, 0, 1, 1, 3, 5, 6, 7, 3, 1]

i = 7
c = count[i] = count[7] = 1;
range() = range(0, 1)
arr[k] = i => arr[6] = 7; k+=1 = 7+1 =8
arr = [0, 0, 1, 1, 3, 5, 6, 7]



```

### Analysis:

`Time Complexity:`: `O(N+N+MAX)`.
`Space Complexity:`: `O(MAX)`.
Count sort algorithm is heavily dependent on maximum element in the array.
for instance if length of the array is `[9` and max element among `9` element is `10^9`, then there had to be a `count array` of size `O(10^9)` and the last loop also runs for `O(10^9)`.

### Application:

- Used for strings, at max there is 52 alphabets and the above concerns are not an issue with less numbers.
