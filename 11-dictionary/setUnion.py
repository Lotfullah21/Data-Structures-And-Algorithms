"""
Given N 2D Points, Calculate no. of distinct points among them.

Ex: x[5] = {2, 1, 3, 2, 2}
    y[5] = {3, 1, 2, 3, 4}
    
The first array represents the x co-ordinates, the second array represents the y co-ordinate. Acoording to above examples the points are 
    (x[0],y[0])->(2,3)
    (x[1],y[1])->(1,1)
    (x[2],y[2])->(3,2)
    (x[3],y[3])->(2,3)
    (x[4],y[4])->(2,4)
    
Total number of distinct points are 4.
"""





def Max_Points(X, Y):
    hs = set()

    for i in range(len(X)):
        hs.add(str(X[i]) + " " + str(Y[i]))
    print(hs)

    return len(hs)

if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    print(Max_Points(x, y))



def main():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    result = union(arr1, arr2)
    print(result)
    
    
    
def union(arr1, arr2):
    setOne = set()
    setTwo = set()
    for ele in arr1:
        setOne.add(ele)
    for ele in arr2:
        setTwo.add(ele)
        
    answer = setOne.union(setTwo)
    return len(answer)

if __name__ == "__main__":
    main()