def myPow(x: float, n: int) -> float:
    """calculate and return power of a number

    Args:
        x (float): The base number
        n (int): The exponent number

    Returns:
        float: base raised to the power of exponent.
    """
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        x = 1 / x
        n = -n
    temp = myPow(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return temp * temp * x


x = int(input("Enter the base: "))
n = int(input("Enter the exponent: "))
print(myPow(x, n))