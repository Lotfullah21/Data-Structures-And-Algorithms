### Question:

## Question:

Given an array of numbers, write a function that takes two parameters: the head none and an element to be inserted at the beginning.
return a new list that contains the list with given element inserted at the beginning.

input: 2>3>5>9>-1
element = -12
output: 2>3>5>9>-1>-12
Explanation: new element is added to beginning of the list.

## Note:

in python, objects are passed by reference, which means if we assign two different variables for the same object, any modification to any of the variables will have an effect on the variable as well. Because both of them are pointing to the same object.

That's why in the following code, even though temp is assigned to the head object, still it changing its next changes the head object as well.

```py
def insertionAtEnd(node: Node, val: int,head: Node) -> Node:
    "insert a node at the end of a the linked list"
    # Temp variable is assigned to temp head object and any change at temp will effect head object as well.
    temp = head
    if head is None:
        head = node(val)
    else:
        while(temp.next != None):
            temp = temp.next
        temp.next = node(val)
        return head

```

### Analysis:

`Time Complexity`: `O(n)` We need to traverse the whole linked list to reach to the end point.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
