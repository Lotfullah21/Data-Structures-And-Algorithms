# 1. Brute Force (Linear Search)
def main():
    array = list(map(int, input("Enter an array: ").split()))
    target = int(input("Enter an integer find the floor for: "))
    print(floor(array, target))
    
def floor(arr: list, k: int) -> int:
    """return the closest value to k from arr list."""
    low = 0
    high = len(arr) - 1
    ans = float("-inf")
    while(low<=high):
        mid = (low + high) // 2
        if arr[mid] == k:
            return k
        elif arr[mid]<k:
            # Remember to update the answer here, because we are looking for just smaller number.
            ans = arr[mid]
            low = mid + 1    
        else:
            # if arr[mid] > k
            high = mid -  1
          
    return ans
if __name__ == "__main__":
    main()








