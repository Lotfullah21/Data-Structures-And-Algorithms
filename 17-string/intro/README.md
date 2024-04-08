#### There are two main functions in to with characters:

- ord("char"): returns ASCII value of the character.
- chr(num): returns the integer representation of a character of a character.

In python, we don't have characters and a single character is just a string with length 1.

In python, unicode is used to represent different characters from different languages, like Farsi, Pashto, Hindi and so many other languages.

### Escape `\`:

When using single quotes to wrap a string, if another single quote is added in between, python considers that as end of the string.

```py

Input: s = 'Afghanistan's mountains'
Output: Syntax Error, because python treats that single quote after Afg as the end of the sequence.

```

##### Two methods:

- Use double quotes
- Use Escape (\) character before the single quote that you don't want to be treated as the end of the sequence.

```py

Input: s = 'Afghanistan\'s mountains'
Output: Afghanistan's mountains;
it does not consider that `'` as the end, but escapes it.
```

#### \n:

It means create a new line.
When `\n` is used, it says does not count `n` as part of the string, escape it and create a new line.

```py

Input: s = 'Afghanistan\'s mountains are:\n Kohi Baba\n, Salang'
Output: Afghanistan's mountains are
        kohi Baba, Salang.;
```

#### \\:

Escape the `\` it self.

```py

Input: s = 'Hello\\';
Output: Hello\
```

```py

Input: s = 'Hello\';
Output: Error, it is escaping `'` which here indicates end of the sequence. If that is escaped, it means the end quote is missing and it causes an error.
```

#### Raw(r):

Raw strings are used dictate to python that process the string as it is and Do not process the `\` or `\t` present inside the string.
By adding `r` or `R`, this can be achieved.

```py

Input: s = 'C:\project\name.py';
Output: C:\Project
        ame.py
```

```py

Input: s = r'C:\project\name.py';
Output: C:\Project\name.py
```

#### Format String

1. Use `+`

```py
subject = "Machine Learning"
Duration = "Four months"
s = subject + " takes " + Duration + " to complete"
print(s)


```

2. Use format

```py
subject = "Machine Learning"
Duration = "Four months"
s = "{} takes {} to complete".format(subject, Duration)
print(s)


```

3. Use F String

   ```py
   subject = "Machine Learning"
   Duration = "Four months"
   s = f"{subject} takes {Duration} to complete"
   print(s)

   ```

Among all, F-string is best.
