## to iterate in reverse direction in range function.

```py
for i in range(n-1, -1, -1):
    # Your code here
    print(i)
```

Start (n-1): It starts from n-1 because Python uses zero-based indexing, and you want to start from the last index.
Stop (-1): It stops at -1 because it doesn't include the value -1 itself. The range will go down to 0 (inclusive).
Step (-1): It means to decrement by 1 in each iteration, effectively moving in the reverse direction.

```py

list = [[1,2,3],[5,6,7,8,9]]

When we use len method, it counts number of rows in a list.
len(list) = 2
when we use len(arr[0]), we count number of columns, Logically it means how many elements are there in first row.
len(arr[0]) = 3
len(arr[1]) = 5


```

In Python, a list is stored in memory as a contiguous block of memory, but what it contains are references to the elements rather than the elements themselves.

The above two lists are referenced by contagious numbers, but the lists themselves might be saved at different location.

Let's say you have a Python list: my_list = [1, 2, 3]

1. Initially, Python might allocate space for 3 pointers in the PyListObject, as there are 3 elements.
2. These pointers would point to the memory locations where 1, 2, and 3 are stored.
3. If you append another element, say 40, and it exceeds the allocated capacity, Python will allocate a new block of memory (larger than the previous), copy 1, 2, 3, and 4 to this new block, and update the pointers.
4. This dynamic resizing allows Python lists to be very flexible, but it's also important to note that it can lead to occasional performance hits, especially if you're repeatedly growing a large list.

- #### Contiguous Block of Memory:

The actual list object itself (PyListObject) is a contiguous block of memory.
This block of memory holds the metadata for the list, such as the size of the list and the capacity.
However, the elements of the list are not stored directly in this block of memory.

- #### References to Elements:

When you add elements to a list, Python stores references to these elements in the contiguous block of memory.
These references are essentially pointers to the memory locations where the actual elements are stored.
This means that a list can hold elements of different data types, and each element can have a different size in memory.

```py
my_list = [10, "hello", [1, 2, 3], {'a': 1, 'b': 2}]
```

The PyListObject for my_list would have a contiguous block of memory that stores:

Size information (how many elements are in the list)
Capacity information (how many elements the list can currently hold before resizing)
References to the elements
For the elements themselves:

10 is an integer, which is a fixed size and has its own memory location.
"hello" is a string, which is also a fixed size and has its own memory location.
[1, 2, 3] is a list, and the reference to this list is stored in the PyListObject block.
{'a': 1, 'b': 2} is a dictionary, and the reference to this dictionary is also stored in the PyListObject block.
