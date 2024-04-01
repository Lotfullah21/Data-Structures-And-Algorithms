arr = [[1, 2, 3],[4, 5, 6, 7, 8]]
for row in arr:
    for col in row:
        print(col,end=" ")
    print()
    
    
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()