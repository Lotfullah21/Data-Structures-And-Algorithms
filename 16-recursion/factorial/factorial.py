
def main():
    n = int(input("Enter a number: "))
    # Handle the case when the user enters an non-positive integer
    if n<0:
        print("Enter a positive number")
        return 
    result = fact(n)
    print(f"{n}! = {result}")
    
    
def fact(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial of the input integer, which is the product of consecutive integers from 1 to n.
    """
    # Base case
    if n==0:
        return 1
    else:
        return n * fact(n-1)

if __name__ == "__main__":
    main()
    

