

def yell(*args: str) -> list:
    """returns upper case of the input arguments

    Returns:
        list: upper cased words
    """
    upperCased = map(str.upper, args)
    print(*upperCased)


def main():
    yell("Hello hyderabad","hello mit")
    
if __name__ =="__main__":
    main()
    
    
    
    
    
# def yell(words):
#     return words.upper()

# def main():
#     print(yell("Hello hyderabad"))
    
# if __name__ =="__main__":
#     main()