# Initialize an array with four elements inside, each filled with -10.
n = [-10] * 4
# Create a row with 5 columns
m = [5] * 5

print("single row",n)
print("single row",m)

x  = []
arr = []
# lets use loops to create a dynamic loop
for i in range(10):
    # Create a list with 10 elements
    x = [i]*10
    # Append the list to current arr.
    arr.append(x)
    
# len(arr[0]) means how many elements are there in first row.
print("number of columns = ",len(arr[0]))
print("number of rows =",len(arr))

# we are having array of arrays in arr, we can index each row by arr[i]
for i in range(len(arr[0])):
    print(arr[i])
    
print(arr)