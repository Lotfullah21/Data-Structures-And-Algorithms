"""a * b means add a b times

a * 4 = a + a + a + a
a * n = a + a + a + a + a + a + a + a + ... + a
a * b = a + a * (b - 1), as we took one a out of b times, so we reduce by one.

if b = 1, then a * 1 = a:
so this can be considered as the base case.

"""

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = mul(a, b)
    print(f"{a} * {b} = {result}")

def mul(a: int, b: int) ->int:
    """using recursion, find the multiplication of two numbers

    Args:
        a (int): a number that needs to be multiplied b times
        b (int): a number that decides how many times, a should be summed.

    Returns:
        int: result of a * b.
    """
    if b == 1:
        return a
    else:
        return a + mul(a, b-1)
        
if __name__ == "__main__":
    main()