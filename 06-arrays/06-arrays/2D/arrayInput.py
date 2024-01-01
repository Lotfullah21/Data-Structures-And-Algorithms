# n, m = map(int, input().split())
n, m = map(int, (input("Enter number of rows and columns: ").split()))
array = []

# taking users input as an array element
for i in range(n):
    # create an array of m*n
    array.append([0]*m)
    for j in range(m):  
        print("row",i,"column",j,end=" ")
        array[i][j] = int(input(""))

    
    
for i in range(n):
    for j in range(m):  
        # print each element until we reach m
        print(array[i][j],end=" ")
    # exit the loop and print a new line when have reached to the end of column.
    print()
    
    
