def main():
    n = int(input(""))
    arr = list(map(int, input().split())) 
    print(maxNumber(arr))
    
def maxNumber(arr):
    firstMax = float('-inf') 
    secondMax = float('-inf') 
    index =0
    for i in range(0,len(arr)):
        if arr[i]>firstMax:
            secondMax = firstMax
            firstMax = arr[i]
            index = i
        elif arr[i]>secondMax:
            secondMax = arr[i] 
    return index if firstMax>=2*secondMax else -1
    
    

if __name__ == "__main__":
    main()