
def reArrange(arr: list, start: int, end: int) -> list:
    """Move all elements smaller than starting index element to the left and larger elements to the right

    Args:
        arr (list): list of integers.
        start (int): start of sub array.
        end   (int): end of sub array.

    Returns:
        list: A modified list that all elements smaller than starting index should move to the left and larger elements to the right.
    """
    n = len(arr)
    p1 = start+1
    p2 = n - 1
    # As long as p1 and p2 did not cross each other, continue.
    while p1<=p2:
        # If element of p1 is smaller than start, increment the p1.
        if arr[p1]<=arr[start]:
            p1+=1
        # If element of p2 is larger than start, decrement the p2. p2 starts from last index.
        elif arr[p2]>arr[start]:
            p2-=1
        else:
            # If none of the above conditions meets, p1 and p2 are not in the right place swap them.
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p2-=1
            p1+=1
    # Swap the oth index element with element at pointer p2.
    temp = arr[start]
    arr[start] = arr[p2]
    arr[p2] = temp
    
arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
start = 4
end = 6
reArrange(arr,start,end)
print(arr)


