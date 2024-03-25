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
        
        
largest = getMax([1, 2, 3, 4, 5, 6])
print("largest element is =", largest)