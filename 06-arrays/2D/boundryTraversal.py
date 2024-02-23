def boundaryTraversal(arr: list) -> list:
    row = len(arr)
    col = len(arr[0])
    if row == 1:
        for i in range(col):
            print(arr[0][i],end=",")
    elif col==1:
        for i in range(row):
            print(arr[i][col],end=",")
    else:
        for i in range(col):
            print(arr[0][i],end=",")
        for i in range(1, row):
            print(arr[i][col-1],end=",")
        for i in range(col-2, -1, -1):
            print(arr[row-1][i], end=",")
        for i in range(row-2,0,-1):
            print(arr[i][0],end=",")
    print()
            
            
arr = [[col+1 for col in range(5)] for row in range(10)]
arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
boundaryTraversal(arr)