"""
Given N elements, Rearrange the array so that

a) arr[start] should go to correct sorted position
b) all elements <=arr[start] should go to left side of arr[start]
c) all elements >arr[start] should go to right side of arr[start]

It does not mean all elements to the right and left hand side should be sorted.
"""
# import random
def reArrangeSubArray(arr: list, start: int, end: int) -> list:
    # start = random.randint(start, end)
    p1 = start + 1
    p2 = end
    while p1<=p2:
        if arr[p1]<=arr[start]:
            p1+=1
        elif arr[p2]>arr[start]:
            p2-=1
        else:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p2-=1
            p1+=1
    temp = arr[start]
    arr[start] = arr[p2]
    arr[p2] = temp
    
    

arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
n = len(arr)-1
reArrangeSubArray(arr, 0, n)
print(arr)