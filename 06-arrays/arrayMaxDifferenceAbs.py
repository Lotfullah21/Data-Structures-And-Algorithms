"""
Given n length array "arr". Find (i,j) with maximum value of (abs(arr[i] - arr[j]) + i - j). You need to print max value of (abs(arr[i] - arr[j]) + i - j) possible and not the (i,j) itself.

Note 1: abs represents the postive part only. ex: abs(8) = 8 and abs(-8) = 8.
"""


def main():
    n = int(input(""))
    arr = list(map(int, input("").split()))
    
    max1 = maxDiff1(arr)
    print("arr1",arr)
    max2 = maxDiff2(arr)
    print("arr2",arr)
    ans = maxDiffAbs(max1,max2)
    print("max1",max1,"max2",max2,"abs",ans)
    

def maxDiff1(arr):
    current_max = float("-inf")
    current_min = float("+inf")
    
    for i in range(len(arr)):
        arr[i] = arr[i] + i
    
    for i in range(len(arr)):
        if arr[i]>current_max:
            current_max = arr[i]
        if arr[i]<current_min:
            current_min = arr[i]
            
    # because we use the same array in second function and we want to bring back the original array
    for i in range(len(arr)):
        arr[i] = arr[i] - i
    
    return (current_max-current_min)
        

def maxDiff2(arr):
    current_max = float("-inf")
    current_min = float("+inf")
    for i in range(len(arr)):
        arr[i] = arr[i] - i 
    for i in range(len(arr)):
        if arr[i]>current_max:
            current_max = arr[i]
        if arr[i]<current_min:
            current_min = arr[i]
            
    return (current_max-current_min)

def maxDiffAbs(diff1, diff2):
    return max(diff1,diff2)



if __name__ == "__main__":
    main()
    