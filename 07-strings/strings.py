# there are two main functions in to with characters.

## 1.  ord("char"): returns ASCII value of the character.
## 2.  chr(num): returns the integer of a character.

char1 = "A"
print(f"Integer value of {char1} is = ", ord(char1))


char2 = "B"
print(f"Integer value of {char2} is = ", ord(char2))


# we can do mathematical operation as well after converting it into integer;
charSummation = ord(char1) + ord(char2)
print(f"{char1} + {char2} =",charSummation)


# we can use chr() to obtain the ASCII character of an integer.
b = chr(90)
print("ASCII character of 90 is",b)


name = "HoshmandLab"

print(name[0])
print(name[-1:])
print(name[0:])



my_string = "This is a test string!"
# split method will be create substrings based on white space, ["This", "is","a","test","string"]
substring = my_string.split() # This
substring0 = my_string.split()[0] # This
print(substring0)
print(substring[0])


my_string_slice = my_string[0:-1]
print(my_string_slice)

# find method is used to get the index related to that particular string.
my_string_this_index = my_string.find("is")
print("index of is = ",my_string_this_index)


# length of a string, it counts number of characters and white spaces as well.
print("length of my_string",len(my_string))
# if we index for a particular number, we will be having only that particular character not the whole word.
print(my_string[0])



print(chr(ord("v")+9))


