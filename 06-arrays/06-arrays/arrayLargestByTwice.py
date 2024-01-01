# pseudo
# ! smart idea
# find largest and 2nd largest, if largest is twice as 2nd largest, it means it can be twice as larger than any other element.

# loop through and check if any element is greater than our initialized largest, if so, swap the values and save the inedx
# ! before swapping: to save the current largest to 2nd largest and update the newly founded max.

def main():
    arr = list(map(int, input("").split()))
    answer = found_largest(arr)
    print(answer)
    
    
def found_largest(arr):
    current_max = float('-inf')
    second_max = float('-inf')
    max_index = 0
    
    for i in range(len(arr)):
        if arr[i]>current_max:
            second_max = current_max
            current_max = arr[i]
            max_index = i
        elif arr[i]>second_max:
            second_max = arr[i]
            
    if current_max>2*second_max:
        return f"{current_max} is twice as every element in {arr} and the index is {max_index}"
    else:
        return f"{current_max} is not twice as larger than every element"


if __name__ == "__main__":
    main()        