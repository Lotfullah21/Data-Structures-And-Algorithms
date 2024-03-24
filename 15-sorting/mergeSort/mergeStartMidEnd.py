"""
Given a sorted arrays with N elements and 3 indices s, m and e such that sub-array [s,m] is sorted, sub-array [m+1,e] is sorted. Sort the sub-array [s,e].

Note: s to m and then m+1 to e are continuous sub-arrays.

"""


def merge(start: int, mid: int, end: int, arr: list) -> list:
    p1 = start
    p2 = mid+1
    p3 = 0
    # Take care of (end-start+1), because start-end+1 is different.
    temp = [[] for _ in range(end-start+1)]

    while(p1<=mid and p2<=end):
        if arr[p1]<arr[p2]:
            temp[p3] = arr[p1]
            p1+=1
            p3+=1
        else:
            temp[p3] = arr[p2]
            p2+=1
            p3+=1
    while (p1<=mid):
        temp[p3]=arr[p1]
        p1+=1
        p3+=1
    while (p2<=end):
        temp[p3] = arr[p2]
        p2+=1
        p3+=1       
    # Copy the temp array elements into main array.
    n = end - start + 1 
    for i in range(n):
        j = start + i
        arr[j] = temp[i]
        
      
    return arr

arr = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
start = 2
mid = 6
end = 9

new_array = merge(start,mid, end, arr)
print(new_array)

