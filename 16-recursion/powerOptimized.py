"""

in prev example, we were reducing the function just by the factor of one, each time base^exponent-1, base^exponent-2, base^exponent-3
but base^exponent = base^exponent/2 * base^exponent/2. in this case, the function is getting divided by 2 each time.
N/2 -> N/4 -> N/8 -> N/16 -> N/32 ... 1; and so one. if we calculate the time complexity for this series it will O(logN)

N/2^k = 1 => N = 2^k => k = log(N .base2) is the number of steps we take until we reach to 1 which is the base case.

we need to consider the negative for exponent as well as it really adds up to our recursive calls, better to define one for it.

pow(2, 3) = 2^3 = 8
pow(3, 2) = 3^2 = 9
 
pow(2, -3) = 2^-3 = (1/2^3) = (1/2)^3
pow(3, -2) = 3^-2 = (1/3^2) = (1/3)^2

we can see the pattern that x is getting divided by 1 and exponent is becoming positive, Hence we can add this condition as well.

you can see another if condition which is checking for odd and even exponents, because if exponent is even, for instance pow(3, 4) = 3^2 * 3^2 and pow(3, 5) != 3^2 * 3^2. 
thus, for odd exponents, we need to multiply the base at the end( temp * temp * x).
"""






def myPow(x: float, n: int) -> float:
    """calculate and return power of a number

    Args:
        x (float): The base number
        n (int): The exponent number

    Returns:
        float: base raised to the power of exponent.
    """
    if n == 0:
        return 1.0
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