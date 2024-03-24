""" Calculate a raised to the power b.

a raised to the power of a number is multiplying a that many times.
a^b = a * a * a * a * ... * b.
2^4 = 2 * 2 * 2 * 2

we can write 2^4 = 2 * 2^3, 
Hence, a^b = a * a^b-1

when b==1, a^b = a^1 = a
Hence, 2^1 = 2. So b==1 can be considered as a bases case where we return 'a' itself,

"""
def main():
    a = int(input("Enter the base: "))
    N = int(input("Enter the power: "))
    ans = power(a,N)
    print(ans)
    
    
def power(base: int, exponent: int) -> int:
    """ Calculate the power of a number using recursion technique.

    Args:
        base (int): The base number 
        exponent (int): The exponent which the base is multiplied that many
    Returns:
        int: Calculate base raised to the exponent.
    """
    if exponent ==1:
        return base
    else:
        return base * power(base, exponent -1 )
        


if __name__ == "__main__":
    main()    
    
    
    


# def main():
#     a = int(input("Enter the base: "))
#     N = int(input("Enter the power: "))
#     ans = power(a,N)
#     print(ans)
    
    
# def power(base: int, exponent: int) -> int:
#     """ Calculate the power of a number

#     Args:
#         base (int): The base number 
#         exponent (int): The exponent which the base is multiplied that many
#     Returns:
#         int: Calculate a to the power of n
#     """
    
#     if base<0:
#         raise ValueError("Exponent should be a non negative integer")
#     ans = 1
#     for i in range(1, exponent+1):
#         ans = ans * base
#     return ans
        


# if __name__ == "__main__":
#     main()    