def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(unique(arr))
    

def unique(arr):
    n = len(arr)
    if arr[0] !=arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]  
    high = len(arr)-2
    low = 1
    while(low<=high):
        mid = (high + low)//2
        if arr[mid+1] != arr[mid] and arr[mid-1]!= arr[mid]:
            return arr[mid]
        if arr[mid] == arr[mid-1]:
            mid = mid - 1
        if mid%2==0:
            low = mid + 2
        else:
            high = mid -1
            
            
            
if __name__ == "__main__":
    main()