def main():
    n = int(input("Enter the year: "))
    is_leap_year(n)
    
def is_leap_year(n: int) -> str:
    """checks if the year is a leap year or not

    Args:
        n (int): an integer that represents year

    Returns:
        str: s sentence mentioning whether the year is a leap year or not based on few conditions.
    """
    if (n%4==0 and n%100!=0) or (n%400) == 0:
        print(f"{n} is a Leap year")
    else:
        print(f"{n} is not a leap year")           
    
if __name__ == "__main__":
    main()