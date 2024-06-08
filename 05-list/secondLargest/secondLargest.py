def getMax(list: list) -> int:
    "Returns the largest element from a list."
    # Check list is empty
    if not list:
        return "LIST EMPTY"
    
    maximum = float("-inf")
    n = len(list)
    for i in range(n):
        if list[i]>maximum:
            maximum = list[i]
    return maximum


def secondLargest(arr: list) -> int:
    firstMax = getMax(arr)
    "Returns the largest element from a list."
    # Check list is empty
    if not list:
        return "LIST EMPTY"
    
    maximum = float("-inf")
    n = len(arr)
    for i in range(n):
        if arr[i]>maximum and arr[i]<firstMax:
            maximum = arr[i]
    return maximum


largest = secondLargest([1, 2, 3, 4, 5, 6])
print("largest element is =", largest)