"""
Question: find the max difference between two elements in the (arr[i] + i - j + arr[j])
Solution: first add each element to its index, arr[i] + i is same as arr[j] + j, both of them are pointing to the same array.
if we add indices to their respective value, that will be counted for j as well.

in fact here, it does not ask us directly to calculate the max difference, first we have to make some modification to the array, then find the difference.

Idea is after modification, find the max and min element of the array and then subtract them.
    
after displacement of above's placeholders

(arr[i] + i - (arr[j] + j)) == (arr[i] + i - j + arr[j])
    
"""

def main():
    n = int(input(""))
    arr = list(map(int, input("").split()))
    print(maxDifference(arr))
    

def maxDifference(arr: list) -> int:
    """it gives us maximum value of arr[i] + i - j + arr[j]
       i & j are max_index and min_index respectively

    Args:
        arr (list): list of numbers given by user

    Returns:
        int: An integer which is the result of max((arr[i]+i)-(arr[j]-j))
    """
    current_max  = float("-inf")
    current_min = float("+inf")
    # original array
    print("original array",arr)
    for i in range(0 , len(arr)):
        # add to each element its indices and modify the original array
        arr[i] = arr[i] + i
    print("new array",arr)
    # check for min and max element in the array
    for i in range(0,len(arr)):
        if arr[i]>current_max:
            current_max = arr[i]         
        if arr[i]<current_min:
            current_min = arr[i]      
    print("max",current_max, "min",current_min)
    
    return (current_max - current_min)

if __name__ == "__main__":
    main()