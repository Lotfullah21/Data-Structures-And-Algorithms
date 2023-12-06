def main():
    n = int(input(""))
    arr = list(map(int, input("").split()))
    start,end = map(int, input().split())
    newarr = reverse(arr, start, end)
    for i in newarr:
        print(i, end=" ")
    
def reverse(arr,start, end):
    
    start = start
    end = end

        
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
            
        start+=1
        end-=1
    return arr

if __name__ == "__main__":
    main()