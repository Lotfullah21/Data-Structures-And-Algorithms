def main():
    arr = list(map(int, input("Enter the  elements: ").split()))
    print(atleastOneMax(arr))
    
def atleastOneMax(arr: list) -> int:
    """counts number of elements that has at least one number greater than themselves.

    Args:
        arr (list): list of integers

    Returns:
        int: total number of elements that are having at least one number greater than itself. 
    """
    max = float("-inf")
    uniqueValues = set()
    count = 0
    for i in range(0,len(arr)):
        if arr[i]>max:
            max = arr[i]
    for i in range(0,len(arr)):
        if arr[i]==max:
            count = count + 1
        # if we want to count only unique values, we can use sets and subtract from len of set.    
        uniqueValues.add(arr[i])
    print(uniqueValues)
    # return len(uniqueValues) - count
    return len(arr) - count
    
if __name__ == "__main__":
    main()