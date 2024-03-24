

# the idea behind finding factorial of a number is multiplying sequential number from beginning until the end of that number starting from 1.
N = int(input("number to find the factorial for ? "))

def factorial(n: int) ->int:
    """returns factorial of a number

    Args:
        n (int): an integer which we want to find the factorial for

    Returns:
        int: multiplication of a number from its beginning which is one till that number itself.
    """
    fact = 1
    for i in range(1,N+1):  
        fact = fact * i
    return fact

fact4 = factorial(4)
print(fact4)
    

