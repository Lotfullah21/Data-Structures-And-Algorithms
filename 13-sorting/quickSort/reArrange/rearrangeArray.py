"""
Given N elements, Rearrange the array so that

a) arr[0] should go to correct sorted position
b) all elements <=arr[0] should go to left side of arr[0]
c) all elements >arr[0] should go to right side of arr[0]

It does not mean all elements to the right and left hand side should be sorted.
"""

def reArrange(arr: list) -> list:
    n = len(arr)
    s = 0
    p1 = 1
    p2 = n - 1
    while p1<=p2:
        if arr[p1]<=arr[s]:
            p1+=1
        elif arr[p2]>arr[s]:
            p2-=1
        else:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p2-=1
            p1+=1
    temp = arr[s]
    arr[s] = arr[p2]
    arr[p2] = temp
    
arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
reArrange(arr)
print(arr)


