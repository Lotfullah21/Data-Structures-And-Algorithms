def boundaryTraversal(self, arr,n,m) -> list:
    row = len(arr)
    col = len(arr[0])
    new_arr = []
    if row == 1:
        for i in range(col):
            print(arr[0][i],end=",")
    elif col==1:
        for i in range(row):
            print(arr[i][0],end=",")
    else:
        for i in range(col):
            print(arr[0][i],end=",")
        for i in range(1, row):
            print(arr[i][col-1],end=",")
        for i in range(col-2, -1, -1):
            print(arr[row-1][i], end=",")
        for i in range(row-2,0,-1):
            print(arr[i][0],end=",")
            
            
            
            


