# print first n natural numbers in ascending order

def main():
    n = int(input("Enter an integer: "))
    printDescending(n)
    # print(ans)
    
    

def printDescending(n: int) -> int:
    """Print natural numbers up to n using recursion.

    Args:
        n (int): The bounding number

    Returns:
        int: a sequence of number
    """
    if n ==1:
        print(1)

    else:
        print(n)
        printDescending(n-1)
    return 
    
          
    
if __name__ == "__main__":
    main()