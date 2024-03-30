def main():
    arr = list(map(int, input().split()))
    

def isSorted(arr, idx, number):
    if (idx ==len(arr)-1):
        return True
    ans = isSorted(arr, idx+1)
    if ans==False:
        return False
    else:
        if arr[idx]<=arr[idx +1]:
            return True
        else:
            return False
     
if __name__ == "__main__":
    main()