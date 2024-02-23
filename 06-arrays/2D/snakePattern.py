arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
n = len(arr)
# Remember, lists are 0 based index, first row is an even row, because it is 0th index, not first index.
for i in range(n):
    if i%2==0:
        for j in range(n):
            print(arr[i][j],end=",")
        print()
    else:
        for j in range(len(arr[0])-1,-1, -1):
            print(arr[i][j],end=",") 
        print()