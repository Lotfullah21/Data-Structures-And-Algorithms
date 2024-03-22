def printBoundary(arr: list) -> list:
    i = 0
    j = 0
    n = len(arr)

    for _ in range(n-1):
        print(arr[i][j],end=" ")
        j+=1

    for _ in range(n-1):
        print(arr[i][j],end=" ")
        i+=1

    for _ in range(n-1):
        print(arr[i][j],end=" ")
        j-=1
        
    for _ in range(n-1):
        print(arr[i][j],end=" ")
        i-=1

arr = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13,14,15,16]]
printBoundary(arr)



