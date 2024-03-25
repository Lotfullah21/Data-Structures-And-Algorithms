def maximumElement(arr,n):
    max = float("-inf")
    for ele in arr:
        if ele>max:
            max = ele
    return max

def minimumElement(arr,n):
    min = float("inf")
    for ele in arr:
        if ele<min:
            min = ele
    return min

