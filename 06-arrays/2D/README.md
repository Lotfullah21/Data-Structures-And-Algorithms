## to iterate in reverse direction in range function.

```py
for i in range(n-1, -1, -1):
    # Your code here
    print(i)
```

Start (n-1): It starts from n-1 because Python uses zero-based indexing, and you want to start from the last index.
Stop (-1): It stops at -1 because it doesn't include the value -1 itself. The range will go down to 0 (inclusive).
Step (-1): It means to decrement by 1 in each iteration, effectively moving in the reverse direction.
