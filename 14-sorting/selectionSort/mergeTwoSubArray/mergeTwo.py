def mergeTwo(array, start: int, mid: int, end: int) -> list:
    "Merge and sort the array from start to end"
    p1 = start
    p2 = mid+1
    p3 = 0
    # Create an array of size e-s
    temp = [0]*(end-start+1)
    print(temp)
    while (p1<=mid and p2<=end):
        if array[p1]<array[p2]:
            temp[p3] = array[p1]
            p1+=1
            p3+=1
        else:
            temp[p3] = array[p2]
            p2+=1
            p3+=1
            
    while p1<=mid:
        temp[p3] = array[p1]
        p1+=1
        p3+=1
    
    while p2<=end:
        temp[p3]=array[p2]
        p2+=1
        p3+=1
    # Copy the elements from temp back to main array.
    for i in range(start,end+1):
        array[i]=temp[i]
    return array
        
# Example Usage
array = [1, 3, 4,0, -1, 2, 5, 8, 9, 10]
start = 0
mid = 2
end = 6
result = mergeTwo(array,start, mid, end)
print("sorted array from",start,"index to",end,"index =",result)
        