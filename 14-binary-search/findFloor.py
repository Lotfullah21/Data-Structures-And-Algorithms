"""
Given an array of N elements and K, from the array N, find the floor element of k which the element itself or closest to K. (num<=k)

"""



# 2. Binary Search
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(floor(arr, k))
    
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
            # remember to update the answer here
            ans = arr[mid]
            low = mid + 1    
        else:
            # if arr[mid] > kff
            high = mid -  1
          
    return ans
if __name__ == "__main__":
    main()








# # 1. Brute Force (Linear Search)
# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     k = int(input())
#     print(floor(arr, k))
    
# def floor(arr, k):
#     low = 0
#     high = len(arr) 
#     ans = float("-inf")
#     for i in range(high):
#         if arr[i] == k:
#             return k
#         elif arr[i]>ans and arr[i]<=k:
#             ans = arr[i]       
#     return ans
# if __name__ == "__main__":
#     main()