"""
reversing an array is combination of multiple swaps.
we have to swap the first index with last index and continue until there is no element left.
[10,20,30,40]

temp = arr[0]
arr[0] = arr[3]
arr[3] = temp    

temp = arr[1]
arr[1] = arr[2]
arr[2] = temp   

as we can see the number of swapping we do is len(arr)//2   

"""

def main():
    n = int(input("Enter the length of the array: "))
    arr = list(map(int, input("Enter an element: ").split()))
    
    print(reverse(arr))
    
def reverse(arr: list) -> list:
    """reverse the element of a given array

    Args:
        arr (list): list of integers to be swapped

    Returns:
        list: a modified list with swapped indices.
    """
    start = 0
    end = len(arr) - 1
    print(end)
        
    while(start < end):
        # swap elements at start and of the indices.
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp    
        # move the indices towards each other  
        start+=1
        end-=1
    return arr

if __name__ == "__main__":
    main()