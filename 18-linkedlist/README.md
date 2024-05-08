## Linked list

An ordered, linear, and non-contagious data structure that each element inside it, has a reference to the its next item.

### Advantages:

Insertion and deletion are done at constant time, because we are having the address of the next element.

### Disadvantages:

Looking for an element is costly since the items are not at contagious locations. Whole elements up to target element should be traversed.
No cache friendly since the elements are not at contagious locations.

In Python, when you pass an object like head to a function, you're passing a reference to that object. In the case of a linked list, this means that the function operates on the same linked list object as the one passed into it. Any changes made to the object within the function will affect the original object outside the function.

### Python Implementation:

An object can be represented using classes in python, initialize a class and build as many objects you want.
inside the class, two attributes are necessary: data field and address field. in data field, the current's object value will be stored and in address field, the address of the next object will be stored.

Usually, the object is written as Node and data field and address field is written data and key next or key respectively.

Initially, address field is initialized as `None`.

```py
class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = None.

# Creating the objects.
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

# Connecting the items
self.head = head
head.next = temp1
temp1.next = temp2

```
