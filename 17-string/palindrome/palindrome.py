def isPalindrome(s: str) -> bool:
    low = 0
    high = len(s)-1
    while low<high:
        if s[low]!=s[high]:
            return False
        else:
            low = low+1
            high = high-1
    return True
    
    
if __name__ == "__main__":
    s = input("Enter a string: ")
    result = isPalindrome(s)
    print(result)
    