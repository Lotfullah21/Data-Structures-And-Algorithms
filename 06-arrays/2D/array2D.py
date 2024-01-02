n = int(input("How many rows? "))
m = int(input("How many columns? "))
array = []
# taking users input as an array element
for i in range(n):
    # create a 1d array, with m elements filed with zeros.
    array.append([0]*m)
    for j in range(m):  
        # assign to each element of the array a value
        print("row",i,"column",j)
        array[i][j] = int(input(""))
print()
print("nested loop to go deeper and get element using its columns and rows")
for i in range(n):
    for j in range(m):  
        # print each element until we reach m
        print(array[i][j],end=" ")
    # exit the loop and print a new line when have reached to the end of column.
    print()
print()
print("Using a single loop, it list of elements") 
for i in range(n):
    print(array[i])
print(array)