def main():
    # n = int(input())
    arr = list(map(int, input("Enter an array: ").split()))
    k = int(input("Enter the element you are looking: "))
    search = searchBinary(arr,k)
    if search:
        print("true")
    else:
        print("false")
    
    
def searchBinary(arr,k):
    low = 0
    high = len(arr) - 1
    while(low<=high):
        mid = (high+low)//2
        if arr[mid] == k:
            return True
        elif arr[mid]>k:
            high = mid - 1
        else:
            low = mid + 1
    return False
    
if __name__ == "__main__":
    main()