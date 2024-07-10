def fibonacci(n: int) -> int:
    """Calculate fibonacci of a number

    Args:
        n (int): a non-negative integer that fibonacci is calculated for.

    Returns:
        int: fibonacci of n.
    """
    a = 0
    b = 1
    count = 0
    while (count < n):
        temp = b
        b = temp + a
        a = temp
        print(a, b)
        count +=1
    return a


print(fibonacci(10))