numberOfDigits = int(input("Length of the array: "))
# initialize an array
sum = 0
arr = [0]*numberOfDigits
for i in range(0,numberOfDigits):
    # add each user's input to the array.
    arr[i] = int(input(f"Enter the element {i}: "))
    sum = sum + arr[i]
    
print("your array: ",arr)
print("sum of the elements: ",sum)



