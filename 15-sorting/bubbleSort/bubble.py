def bubbleSort(arr: list) -> list:
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
                


result = bubbleSort([1,3,5,7,8])
print(result)