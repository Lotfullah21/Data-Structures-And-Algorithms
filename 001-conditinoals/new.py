def main():
    n = int(input(""))
    reverseDigit(n)

def reverseDigit(n: int) -> int:
    """Prints the reversed digits of a given number entered by the user.

    Args:
        n (int): An integer entered by the user.
    """  
    while (n > 0):
        rem = n % 10
        n = n // 10
        print(rem, end="")

if __name__ == "__main__":
    main()
