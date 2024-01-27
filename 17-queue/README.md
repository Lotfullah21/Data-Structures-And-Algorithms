```py
    def dequeue(self,q):
        if len(q) ==0:
            return -1
        x = q.pop(0)
        return x
```

In the above code, even though we are assigning the result of pop operation into x and only returning it, still when we call the function, the main list(q) will be effected as a result.
using pop, popleft, push, and all other operations in a list will affect the original list
when we use

```py
myList = [1, 2, 3, 5]
prevList = myList.pop()
# Now, myList has changed, because we used pop()
print(myList) # [1,2,3]
print(prevList) # [5]

```
