### Sorting:

in python there are two methods to sort the elements

1. ##### sort()

- Works only for list.
- Sort in place

2. ##### sorted()

- Works on any iterables.
- Does not modify the list.

Both of them uses TrimSort algorithm which is combination of merge and bubble sorting algorithms.

1. #### Sort():

```py
l1 = [1, 4, 5, 3, 0]
l1.sort() // [0, 1, 3, 4, 5]
l1.sort(reverse=True) // [5, 4, 3, 1, 0]
```

A function also can be passed as a key to the sort method and based on the returned value of that function, the list will be sorted.

```py

def basedOnLength(s):
    return len(s)
l_1 = ["rohid","king", "ayaan-ali"]
l_1.sort()
print(l_1)
l_1.sort(key=basedOnLength)
print(l_1)

Strings are sorted based on the ASCII value of each character, for instance `a` has lower ASCII value than `z`, so in natural order, z will be at the end of the list.
```

```py
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Key function to be included in sort method and based on returns of this, the sorting is done.
def myCoordinates(coordinate):
    return coordinate.x

l = [Coordinate(2, 3),Coordinate(1, 12),Coordinate(2, 3),Coordinate(4, 7),Coordinate(1, 5)]
# Each object inside l will be passed to the myCoordinate function and based on return of this, sorting is done.
l.sort(key=myCoordinates)

for i in l:
    print(i.x, i.y)
Output:

1 12
1 5
2 3
2 3
4 7

```

### Stability:

in the above output, it can bee seen that (1,12) comes before (1, 5), since the sorting is done based on the key, hence the original order is intact. This is called `stability`.
it can be overwritten by some method, for instance in the following example, it can be noticed.

Using built-in methods.
For instance, the `__lt__` provided in the given class, if is passed, there is no need of writing a separate function and passing that.
When Coordinate objects are passed, the sort will consider `__lt__` and based on it, the sorting is done.

```py
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self,other):
        # sorting is done based on smallest x's/
        return self.x<other.x
l = [Coordinate(2, 3),Coordinate(1, 12),Coordinate(2, 3),Coordinate(4, 7),Coordinate(1, 5)]
l.sort()

for i in l:
    print(i.x, i.y)

Output

1 12
1 5
2 3
2 3
4 7
```

```py

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self,other):
        # If x values are same, sort based on lower y values.
        if self.x==other.x:
            return self.y<other.y
        else:
            return self.x<other.x

l = [Coordinate(2, 3),Coordinate(1, 12),Coordinate(2, 3),Coordinate(4, 7),Coordinate(1, 5)]

l.sort()

for i in l:
    print(i.x, i.y)

```

### sorted():

This method works for any kind of iterable and always returns a list.

```py
d = {1:"gfg",2:"leetcode",3:"hoshmandlab"}
# Sorts based on the keys.
new_dict = sorted(d)
print(new_dict, type(new_dict))
Output:
[1, 2, 3] <class 'list'>
```
