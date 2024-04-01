def reverseList(arr: list) -> list:
    "Reverse the given list"
    start = 0
    end = len(arr)-1
    while start<end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1
    return arr


array = [1, 2, 3, 4, 5, 6, 7]
reversed = reverseList(array)
print("Reversed list", reversed)