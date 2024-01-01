# initialize an array using empty list
n = int(input("Enter length of the array: "))
arr = [0]*n
for i in range(n):
    arr[i] = i


print("array",arr)


# using append method
arr1 = []
for i in range(n):
    # using append, because the array is empty, the elements cannot be added using indexing.
    arr1.append(i*10//10)

print("array1",arr1)

# declare arr2
arr2 = [0]*n
for i in range(n):
    arr2[i] = int(input("Enter a number: "))
    
print("array-2",arr2)

# create arr3
arr3  = [0 for _ in range(n)]
for i in range(n):
    arr3[i] = (i+1)*100
print("array-3",arr3)