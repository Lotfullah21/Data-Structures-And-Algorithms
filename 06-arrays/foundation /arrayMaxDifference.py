def main():
    arr = list(map(int, input("").split()))
    print(maxDifference(arr))
    

def maxDifference(arr):
    current_max  = float("-inf")
    current_min = float("+inf")
    max_index = 0
    min_index = 0
    for i in range(0,len(arr)):
        if arr[i]>current_max:
            current_max = arr[i]
            max_index = i

    for j in range(0, len(arr)):
        if arr[j]<current_min:
            current_min = arr[j]
            min_index = j
    print("max",current_max, "min",current_min)
    
    return (current_max - current_min + max_index - min_index)
    
    

if __name__ == "__main__":
    main()