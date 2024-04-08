## Strings

A string is a sequence of characters.
Strings can contain letters, numbers, and symbols, and they are often used for tasks such as input/output, text processing, and data manipulation.

Strings are immutable which means that once created, directly it cannot be changed.

```py
string = "Hi"
string[0]="A" // Error, cannot change string value once assigned.
```

## Character

a "character" refers to a single unit of data that typically represents a letter, digit, or symbol. Characters are the basic building blocks of strings and are often encoded using standard character encodings like ASCII or Unicode.

`difference between name[-1] and name[-:]` => `name[-1]`: This syntax retrieves the character at the last index of the string directly. It returns a single character.
`name[-1:]`: This syntax retrieves a substring starting from the last index to the end of the string. It returns a string that contains only the last character.

### map:

it a applies a function to each element in the iterable and returns an iterable object, not the elements itself, if you want to get the elements, either directly convert to iterable objects like list or tuple or use for loop to get each element.

```py
result = map(int, ['1', '2', '3', '4', '5'])
print(result) # <map object at 0x...>
for num in result:
    print(num)
    1
    2
    3
    4
    5
```

or

```py

result = tuple(map(int, ['1', '2', '3', '4', '5']))
print(result)
(1,2,3,4,5)

result = list(map(int, ['1', '2', '3', '4', '5']))
print(result)
[1,2,3,4,5]

```

or

```py
result_list = list(result)
print(result_list)

```

## whitespace

```py
stringOne = input("Enter you string: ")

for i in stringOne:
    print(i)

# even spaces are counted as characters

h
e
l
l
o

w
o
r
l
d
```

## ASCII (American Standard Code for Information Interchange):

is a character encoding standard that assigns numeric values to various characters, including letters, digits, punctuation marks,
and control characters. It provides a way to represent text in computers and communication equipment.

In ASCII, each character is assigned a unique numeric value, known as its ASCII code or ASCII value

The ASCII value for 'A' is 65 and for 'Z' 90.
The ASCII value for 'a' is 97 and for 'z' 122.
The ASCII value for '0' is 48 and for '9' 57
The ASCII value for space (' ') is 32.
The ASCII value for the exclamation mark ('!') is 33.

behind the scene every character will be converted to its ASCII representation and from ASCII value to binary numbers (machine language).

we have few handy functions in python to convert a char to its ASCII value and vice versa.

```py
ord("character") # gives ASCII value
print(ord("A")) # 65
print(ord(" ")) # 32
print(ord(""))  # error, expects a char
```

```py
char(number) # gives ASCII character represented by that value.
print(chr(65)) # "A"
print(chr(32)) # " "
print(chr(z))  # 122
```

```py
str("data types") # convert a the given data type to a string
print(str(65)) # "65"
print(str(32)) # "32"
print(str(122))  # "122"
```

<!-- but If you want covert from a string to another data type, that data type should be convertible -->

```py
str("data types") # convert a the given data type to a string
print(int("12")) # 65
print(int("0")) # 0
print(int("abc"))  # error, cannot convert an alphabet to integer (invalid literal for int() with base 10: 'abc')
```
