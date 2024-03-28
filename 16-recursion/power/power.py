
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