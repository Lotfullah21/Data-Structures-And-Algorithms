"""a * b means add a b times
2*4 means add 2, four times
2 * 4 = 8
2 + 2 + 2 + 2 = 8
"""

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = mul(a, b)
    print(f"{a} * {b} = {result}")

def mul(a: int, b: int) ->int:
    """this function returns the multiplication of a and b, not by directly multiplying them, but by adding a ,b times to itself.

    Args:
        a (int): the number we want to find its multiple
        b (int): the number that decides how many times a should be summed

    Returns:
        int: summation of a, b times.
    """
    result = 0
    while(b>0):
        result = result + a
        b = b -1
    return result
        
if __name__ == "__main__":
    main()