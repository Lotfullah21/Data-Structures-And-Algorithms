# initialize an array with four elements inside, each filled with zeros.
n = [0] * 4
# it represents a single row
m = [0] * 5
print(n)
print(m)

x  = []
arr = []
# lets use loops to create a dynamic loop
for i in range(10):
    # if we print outside the loop, it gives us only the [9,9,...]
    x = [i]*10
    # it saves all the elements inside the array
    arr.append([i]*10)
print(x)
print(arr[1])

# len(arr[0]) means how many elements are there in first row.
print("number of columns = ",len(arr[0]))
print("number of rows =",len(arr))
# we are having array of arrays in arr, we can index each row by arr[i]
for i in range(len(arr[0])):
    print(arr[i])