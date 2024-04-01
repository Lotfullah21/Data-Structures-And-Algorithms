def minCost(array: list) -> int:
    "Remove the elements in such an order that the total cost is minimum at the end."
    answer = 0
    n = len(array)
    array.sort()
    for i in range(n-1, -1, -1):
        contribution = n - i
        answer = answer + array[i]*contribution
    return answer
        
array = [5,1, 2, 3, 4]
result = minCost(array)
print("the optimal cost after removing elements in optimal order =",result)



