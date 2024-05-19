def mergeTwoSortedArray(arr1: list, arr2: list, n, m) -> list:
    "merge two sorted arrays."
    p1 = 0
    p2 = 0
    p3 = 0
    temp = [[] for _ in range((n+m))]
    # Check until the elements are present in both fo the lists.
    while (p1<n and p2<m):
        if arr1[p1]<arr2[p2]:
            temp[p3] = arr1[p1]
            p1+=1
            p3+=1
        else:
            temp[p3] = arr2[p2]
            p2+=1
            p3+=1
    # After the above loop is finished, one of the loops is going to be empty, now if that non-empty one is array-1, put its elements inside temp.
    while (p1<n):
        temp[p3] = arr1[p1]
        p1+=1
        p3+=1
    # After the above loop is finished, one of the loops is going to be empty, now if that non-empty one is array-2, put its elements inside temp.
    while (p2<m):
        temp[p3] = arr2[p2]
        p2+=1
        p3+=1
    return temp
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
n = 4
m = 5
new_arr = mergeTwoSortedArray(arr1,arr2, n, m)
print(new_arr)

