# 1.Take as input String.

# Write a code that inserts between each pair of characters the difference
# between their ascii codes. Print the final string.

# Note: You can use adding at the end of the string

# Example:

# Input:
# abfk

# output
# a1b4f5k

# 1 = b-a
# 4 = f-b
# 5 = k-f


def main():
    input_string = input("Enter a text: ")
    result  = addInBetween(input_string)
    print(result)
    
    
def addInBetween(old_str):
    new_str = ""
    for i in range(len(old_str)-1):
        char = old_str[i]
        new_str = new_str + char
        ascii_val = ord(old_str[i+1]) - ord(old_str[i])
        new_str = new_str + str(ascii_val)
        print("ascii = ",ascii_val,"char = ",char, "new_Str = ",new_str,"ord i + 1 = ", ord(old_str[i+1]),"ord i = ", ord(old_str[i]))
    new_str = new_str + old_str[-1]
    return new_str
    


if __name__ == "__main__":
    main()