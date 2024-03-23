class Palindrome:
    def isPalindrome(self, number: int) -> int:
        temp = number
        reversed = 0
        while temp>0:
            lastDigit = temp%10
            reversed = reversed * 10 + lastDigit
            temp = temp//10
        if reversed == number:
            return True
        
        
palindrome = Palindrome()
number = int(input("Enter a number: "))
result = palindrome.isPalindrome(number)
if result:
    print("It is a palindrome number")
else:
    print("Not a palindrome number")