stringOne = input("Enter you string: ")

for i in stringOne:
    print(i)
    
# Even spaces are counted as characters
print("Empty space",ord(" "))

for char in "AaZz":
    print(char,ord(char))
