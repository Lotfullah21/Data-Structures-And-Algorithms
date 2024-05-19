def goodIntegers(arr: list) -> list[int]:
    "Returns number of good integers"
    n = len(arr)
    goodIntegers = []
    smallerNumbersCount = 0
    smallerGoodIntegerCounts = 0
    # Taking care of the edge case, at 0th, we will be 0 number that is smaller than the 0 itself.
    if arr[0]==0:
        smallerGoodIntegerCounts+=1
    for i in range(n):
        # Only update smallerCounts variable when the element is occurring for the first time.
        if arr[i]!=arr[i-1]:
            smallerNumbersCount = i
        # If not first occurrence, do nothing.
        else:
            pass
        # If current element has same value as smaller count, it is a good integer.
        if arr[i]==smallerNumbersCount:
            goodIntegers.append(arr[i])
            smallerGoodIntegerCounts +=1
    return goodIntegers, smallerGoodIntegerCounts


arr = [-1, -2, 2, 2, 4]
integers, totalGoodIntegers = goodIntegers(arr)
print("Good integers =", integers, "Total Good integers =", totalGoodIntegers) 