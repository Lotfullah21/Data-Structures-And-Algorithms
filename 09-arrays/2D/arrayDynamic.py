n = int(input("How many rows? "))
m = int(input("How many columns? "))
array = []

for i in range(n):
    # create an array of m*n
    array.append([0]*m)
    for j in range(m):  
        # assign to each element of the array a value
        array[i][j] = i + j
        # print each element until we reach m
        print(array[i][j],end=" ")
    # exit the loop and print a new line when have reached to the end of column.
    print()