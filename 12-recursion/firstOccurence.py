def main():
    arr = list(map(int, input().split()))
    number = int(input())
    ans = firstOccurrence(arr, 0, number)

def firstOccurrence(arr, idx, number):
    if (idx ==len(arr)):
        return -1
    ans = firstOccurrence(arr, idx+1, number)
    
    if arr[idx] ==number:
        return idx
    else:
        return ans
    
    
    
if __name__ == "__main__":
    main()