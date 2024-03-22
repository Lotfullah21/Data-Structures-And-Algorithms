def main():
    s = input("")
    start = 0
    end = len(s)-1
    result = isPalindrome(s,start,end)
    if result:
        print("true")
    else:
        print("false")
def isPalindrome(s,start, end):
    """checks if a string is a palindrome or not

    Args:
        s (_type_): input string.
        start (_type_): starting index of string.
        end (_type_): end index of the string.

    Returns:
        _type_: a boolean value, true if the string is palindrome and false if not palindrome.
    """
    if start == end:
        return True
    if start>end:
        return True
    
    if s[start] == s[end]:
        temp = isPalindrome(s, start+1, end-1)
        return temp
    else:
        return False    
    
    
if __name__ == "__main__":
    main()