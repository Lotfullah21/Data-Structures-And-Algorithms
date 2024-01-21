def main():
    n = int(input("Enter a number: "))
    result = fibonacci(n)
    print(result)
    
    
def fibonacci(n: int) -> int:
    """Calculate fibonacci of a number

    Args:
        n (int): a non-negative integer that fibonacci is calculated for.

    Returns:
        int: fibonacci of n.
    """
    if n ==0 or n==1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    main()





# solutions that does not use recursion.


if __name__ == "__main__": 
    main()
    
    
def main():
    n = int(input("Enter a number: "))
    result = fibonacci(n)
    print(result)
    
    
def fibonacci(n: int) -> int:
    """Calculate fibonacci of a number

    Args:
        n (int): a non-negative integer that fibonacci is calculated for.

    Returns:
        int: fibonacci of n.
    """
    a = 0
    b = 1
    count = 0
    while (count < n):
        temp = b
        b = temp + a
        a = temp
        count +=1
    return a


if __name__ == "__main__": 
    main()
    
    

# using series
    
def fib(n):
    fib_series = [0,1]
    while len(fib_series)<n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series

n = int(input("Enter a fib"))
print(fib(n))