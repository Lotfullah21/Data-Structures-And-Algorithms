def main():
    n = int(input("Enter the length of the array: "))
    arr = list(map(int, input().split()))
    k = int(input(""))
    k = k % len(arr)
    
    # reverse the whole array
    wholeArrayReversed = reverse(arr, 0, len(arr)-1)
    upToKthReversed = reverse(arr, 0, k-1)
    afterKthReversed = reverse(arr, k, len(arr)-1)
    print(arr)
    
def reverse(arr, start, end):
    start = start
    end = end
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end-=1
    return arr

if __name__ == "__main__":
    main()