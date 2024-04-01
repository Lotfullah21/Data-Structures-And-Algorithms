def goodIntegers(arr: list) -> list[int]:
    """Returns list of numbers that its value is equal to number of elements less than themselves.

    Args:
        arr (list): list of integers, non-repeated

    Returns:
        list[int]: list of good integers
    """
    n = len(arr)
    goodIntegers = []
    arr.sort()
    for i in range(n):
        if arr[i]==i:
            goodIntegers.append(arr[i])
    return goodIntegers


arr = [-1, -2, 2, 3 ,4]
result = goodIntegers(arr)
print(result)