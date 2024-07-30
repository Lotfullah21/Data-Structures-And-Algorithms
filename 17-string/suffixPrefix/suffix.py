def suffix(s: str):
    for i in range(len(s)):
        print(s[i:])

        
s = "Hello"
suffix(s)


print("From second function")


def suffix(s: str):
    for i in range(len(s)):
        print(s[len(s) - i - 1:])
        
s = "Hello"
suffix(s)