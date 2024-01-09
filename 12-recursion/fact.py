"""

factorial(4) = 1 * 2 * 3 * 4
factorial(5) = 1 * 2 * 3 * 4 * 5
factorial(5) = 5 * factorial(4) => n * factorial(n - 1)
base case: if n ==1: return and do not call another function. 
after reaching the base case, the flow will be in reverse direction.

"""
def main():
    n = int(input("Enter a number: "))
    result = fact(n)
    print(result)
    
    
def fact(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial of the input integer, which is the product of consecutive integers from 1 to n.
    """
    if n ==1:
        return 1
    else:
        return n * fact(n-1)

if __name__ == "__main__":
    main()
    
    
    
    

# def main():
#     n = int(input("Enter a number: "))
#     result = fact(n)
#     print(result)
    
    
# def fact(n: int) -> int:
#     """returns the factorial of number which consecutive multiplication of that number. 

#     Args:
#         n (int): an integer to find its factorial.

#     Returns:
#         int: a number that is result of iterating through all int numbers up to n.
#     """
#     res  = 1
#     for i in range(1,n+1):
#         res = res * i
#     return res

# if __name__ == "__main__":
#     main()