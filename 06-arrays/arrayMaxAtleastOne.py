def main():
    arr = list(map(int, input("Enter the  elements: ").split()))
    print(atleastOneMax(arr))
def atleastOneMax(arr):
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