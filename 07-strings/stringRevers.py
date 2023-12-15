def main():
    string = input("Enter a string: ")
    reversed_string = reverse(string)
    print(reversed_string)
    
def reverse(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

if __name__ == "__main__":
    main()
    
    
    
    
    # def reverse(string):
    # reversed_str = string[::-1]
    # return reversed_str
