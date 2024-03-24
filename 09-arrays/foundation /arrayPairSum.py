def main():
    arrayLength = int(input("Enter length of the array: "))
    arr = list(map(int, input().split()))
    k = int(input("Enter the sum you want to get"))
    
    result  = pairSum(arr, k)
    result  = pairSum(arr, k)
    print("true" if result else "false")
    
def pairSum(arr, k):
    
    """
    input: an array with length n
    output: true if there is two index value that sums up to a number.
    
    """
    for i in range(0,len(arr)):
        for j in range(i + 1,len(arr)):
            print ("i = ",arr[i], "j = ",arr[j],"i+j = ",arr[i]+arr[j])
            if arr[i] +  arr[j] == k:
                print("Founded index","i = ",i,"j = ",j)
                return True
    # tricky point is to where we have to place false condition, we are putting here so that all numbers from inner and outer loop had been checked.
    return False 
    

if __name__ == "__main__":
    main()