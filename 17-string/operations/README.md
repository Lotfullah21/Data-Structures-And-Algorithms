#### Substrings:

A substring is a continuous part of a a larger strings

```py
s1 = "Hello kabul"
s2 = "kab"
# Is s2 is a substring of s1.
print(s2 in s1) // True, because kab is there in s1.
print(s1 in s2) // False, some part like kab, but not the whole part.
```

#### Concatenation:

Use `+` operator to concatenate two strings.

```py
s1 = "Hello"
s2 = "World"

print(s1+s2) // Hello world.
```

#### Finding Position index():

It returns the index of the substring we are looking for, if not present, returns - 1.

```py
s1 = "Hello World"
s2 = "Hello"
# Returns the first occurrence substring s2 in s1.
print(s1.index(s2)) // 0, Because it starts with 0.
```

#### s.lower(), s.upper(), s.islower(), s.islower():

```py

s = "Hello World"
s.lower() // hello world.

s = "Hello World"
s.upper() // HELLO WORLD

s = "Hello World"
s.islower() // False, every single character should be lower case letter.

s = "Hello World"
s.isupper() // False, every single character should be upper case letter.


```

#### Starts and Ends With

Returns a boolean value if a string starts or ends with a substring.

```py
s = "Hello world"
s.startswith("Hello") // True
s.endswith("world") // True
# Does string s starts with "Hello" starting from index 1.
s.startswith("Hello", 1) // False

```

#### Split and Join

It joins the elements of a string and returns a list of them.

```py
s  = "Hello World"
s.split() // ["Hello","World"]
s = "Pen, book, notebook"
# Split based on , and space.
s.split(", ") // ["Pen, book, notebook"]
```

###### Join:

It joins elements of a list into a string.

```py
s  =  ["Hello","World"]
# Join each element from the list and add a space after each element added.
s = " ".join(s) // "Hello World"
# Split based on , and space.
s.split(", ") // ["Pen, book, notebook"]
```

#### Find()

It searches for a substring inside a another string, if that sub string is present, it returns the first occurrence of that, if substring is not present it return -1.
In case of

```py
s = "Pen, book, notebook"
s.find("pen") //0
s.find("ook") //-1, Not present.
```
