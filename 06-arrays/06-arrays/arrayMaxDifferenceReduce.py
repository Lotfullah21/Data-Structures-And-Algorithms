"""
Question: find the max difference between two elements in the (arr[i] - i - j + arr[j])
Solution: first subtract each element from its index, arr[i] - i is same as arr[j] - j, both of them are pointing to the same array.
if we add indices to their respective value, that will be counted for j as well.

in fact here, it does not ask us directly to calculate the max difference, first we have to make some modification to the array, then find the difference.

Idea is after modification, find the max and min element of the array and then subtract them.
    
after displacement of above's placeholders:=> (arr[i] - i) - (arr[j] + j)) == (arr[i] + i - j + arr[j])
    
"""

def main():
    n = int(input(""))
    arr = list(map(int, input("").split()))
    print(maxDifference(arr))
    

def maxDifference(arr: list) -> int:
    current_max  = float("-inf")
    current_min = float("+inf")
  
    print("prev array",arr)
    for i in range(0 , len(arr)):
        # subtract each element from its indices.
        arr[i] = arr[i] - i
    print("new array",arr)
    for i in range(0,len(arr)):
        if arr[i]>current_max:
            current_max = arr[i]         
        if arr[i]<current_min:
            current_min = arr[i]      
    print("max",current_max, "min",current_min)
    
    return (current_max - current_min)

if __name__ == "__main__":
    main()