def main():
    n = int(input("Enter a number: "))
    result = total(n)
    print(result)
    
    
def total(n: int) -> int:
    """Calculate the sum of first n integers.

    Args:
        n (int): A non-negative integer for which the summation is calculated up to.

    Returns:
        int: summation of integers.
    """
    if n == 1:
        return 1
    else:
        return n + total(n-1)

        

if __name__ == "__main__":
    main()
    
    
    
# def main():
#     n = int(input("Enter a number: "))
#     result = total(n)
#     print(result)
    
    
# def total(n: int) -> int:
#     """Calculate the sum of first n integers.

#     Args:
#         n (int): A non-negative integer for which the summation is calculated up to.

#     Returns:
#         int: summation of integers.
#     """
#     sum = 0
#     for i in range(1, n + 1):
#         sum = sum + i
#     return sum
        

# if __name__ == "__main__":
#     main()
    
    
    
    
    