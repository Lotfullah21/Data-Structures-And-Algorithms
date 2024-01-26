```py
    def dequeue(self,q):
        if len(q) ==0:
            return -1
        x = q.pop(0)
        return x
```

In the above code, even though we are assigning the result of pop operation into x and only returning it, still when we call the function, the main list(q) will be effected as a result.
