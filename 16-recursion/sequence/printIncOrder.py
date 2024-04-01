# print first n natural numbers in ascending order

def main():
    n = int(input("Enter an integer: "))
    printAscending(n)
    # print(ans)
    
    

def printAscending(n: int) -> int:
    """Print natural numbers up to n using recursion.

    Args:
        n (int): The bounding number

    Returns:
        int: a sequence of number
    """
    if n ==1:
        print(1)

    else:
        printAscending(n-1)
        print(n)
    return 
    
          
    
if __name__ == "__main__":
    main()