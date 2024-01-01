def main():
    n =int(input("Enter length of the array: "))
    array = list(map(int, input("Enter array elements: ").split()))
    start, end = map(int,(input("Start: ? End: ?: ").split()))
    reversed_array = reverse(array,start,end)
    print(array)
    
    
def reverse(arr: list ,start: int, end: int) -> None:
    """
    Reverse an array in-place

    Args:
        arr (list): list of integers to be reversed.
        start (int): the point where reversing indices starts.
        end (int): the point where the reversing stops.
    Return:
        as we referencing to the same array, we do not need to return a new array, any modification here reflects in the main array in heap
    """
    # initialize the points
    start = start
    end = end
    while(start<end):
        # swap the elements at the specified indices.
        temp = arr[start]
        arr[start]  = arr[end]
        arr[end] = temp
        # change the start and end point after each iteration 
        start = start + 1
        end = end - 1  
    # return arr
        
if __name__ == "__main__":
    main()