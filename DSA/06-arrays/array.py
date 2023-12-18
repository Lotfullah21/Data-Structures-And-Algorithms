arr = [0]*10 # initialize an array with 10 elements each assigned zero as a value.
print("an empty array",arr)




arr = [0]*10 # initialize an array with 10 elements each assigned zero as a value.
for i in range(6):
    # for each indices add the corresponding i
    arr[i]= i
print("second array",arr)



arr = [0]*10 # initialize an array with 10 elements each assigned zero as a value.
for i in range(10):
    # for each indices add the corresponding i
    arr[i]= i
print("third array =",arr)




# Using append method.
arr1 = [0] # initialize an empty array
for i in range(6):
    # for each indices add the corresponding i
    arr1.append(i)
print("second array",arr)



# first index should be always equal to 0.
arr10 = [0]*5
for i in range(0,5):
    arr10[i] = (i+1) * 10
print(arr10)




# Taking the number of integers as input
num_integers = int(input("Enter the number of integers: "))

# Initializing an array with zeros
arr = [0] * num_integers

# Using a for loop to take input for each integer
for i in range(num_integers):
    arr[i] = int(input(f"Enter integer {i + 1}: "))

# Printing the resulting array
print(arr)
