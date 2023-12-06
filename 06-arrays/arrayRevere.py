def main():
    n = int(input("Enter the length of the array: "))
    arr = list(map(int, input("Enter an element: ").split()))
    
    print(reverse(arr))
    
def reverse(arr):
    start = 0
    end = len(arr) - 1
    print(end)
        
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
            
        start+=1
        end-=1
    return arr

if __name__ == "__main__":
    main()