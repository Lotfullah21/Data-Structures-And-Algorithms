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


# we can use str() to 