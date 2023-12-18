n = int(input("Enter length of the array: "))
arr = [0]*n

index1 = int(input("swap index 1: "))
index2 = int(input("swap index 2: "))

for i in range(0, n):
    arr[i] = int(input(f"Enter digit {i}: "))
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    
print(arr)
