n,m = map(int,input("How many rows? ").split())
array = []

# taking users input as an array element
for i in range(n):
    # create an array of m*n
    array.append([0]*m)
    for j in range(m):  
         # assign to each element of the array a value
        print("row",i,"column",j)
        array[i][j] = int(input(""))
        # array[i][j] = int(input("Enter a value"))
    
    
for i in range(n):
    for j in range(m):  
        # print each element until we reach m
        print(array[i][j],end=" ")
    # exit the loop and print a new line when have reached to the end of column.
    print()
    
    
x = int(input("Enter"))
print(type(x))

y = int(input().split())
print(type(y))

