def sortArr(arr: list) -> list:
    "Sort an array of 0's, 1's and 2's"
    n = len(arr)
    temp = []
    for ele in arr:
        if ele==0:
            temp.append(ele)
    for ele in arr:
        if ele==1:
            temp.append(ele)
    for ele in arr:
        if ele==2:
            temp.append(ele)
    for i in range(n):
        arr[i] = temp[i]
    return arr


arr = [0,1,2,2,2,0,0,0,0,1,1,1,1]
result = sortArr(arr)
print(result)