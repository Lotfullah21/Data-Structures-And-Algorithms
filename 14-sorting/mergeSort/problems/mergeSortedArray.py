def mergeTwoSortedArray(arr1: list, arr2: list) -> list:
    "merge two sorted arrays."
    p1 = 0
    p2 = 0
    p3 = 0
    n = len(arr1)
    m = len(arr2)
    c = [[] for _ in range((n+m))]
    print(c)
    while (p1<n and p2<m):
        if arr1[p1]<arr2[p2]:
            c[p3] = arr1[p1]
            p1+=1
            p3+=1
        else:
            c[p3] = arr2[p2]
            p2+=1
            p3+=1
    while (p1<n):
        c[p3] = arr1[p1]
        p1+=1
        p3+=1
    while (p2<m):
        c[p3] = arr2[p2]
        p2+=1
        p3+=1
    return c
array_1 = [1, 2, 3, 4]
array_2 = [5, 6, 7, 8]
new_arr = mergeTwoSortedArray(array_1,array_2)
print(new_arr)
# print(new_arr)
# start = 2
# mid = 6
# end = 9
# temp = [[] for _ in range(end-start+1)]
# print(temp)