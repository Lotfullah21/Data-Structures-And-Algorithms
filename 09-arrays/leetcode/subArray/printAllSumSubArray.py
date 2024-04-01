def printSubArraySum(arr: list) -> list[int]:
    n = len(arr)
    subarray_sum = []
    for s in range(n):
        sum = 0
        for e in range(s, n):
            # It just adds the sum, it does not generate sub arrays.
            sum += arr[e]
            subarray_sum.append(sum)
    return subarray_sum

arr = [1, 2, 3, 4]
result = printSubArraySum(arr)
print(result)



