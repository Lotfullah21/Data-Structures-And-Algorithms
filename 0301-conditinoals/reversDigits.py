## Pseudo
# dividing a number%10 gives its last digit (remainder)
# dividing a number//10 removes last digit (take only whole digit)
# previous_value * 10 + rem gives a digit in reverse.



def main():
    n = int(input("enter a number "))
    
def countDigit(n: int) ->int:
    """it reverses a given number entered by user

    Args:
        n (int): an integer entered by user
        
    Returns:
        int: reversed of the input integer
    """
    ans = 0
    while (n>0):
        rem = n%10
        n = n//10
        ans = ans * 10 + rem
    return ans        
if __name__ =="__main__":
    main()