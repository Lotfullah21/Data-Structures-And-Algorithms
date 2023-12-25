# *
```py *``` can be used in function arguments to pass expand the passed arguments as individual elements to the function.

```py
numbers = [12,12,20]
print(total(numbers[0],numbers[1],numbers[2]))
```


<!-- unpacking a list -->
```py
numbers = [12,12,20]
print(total(*numbers))
```

# **
```py **``` it is used to unpack the value of a dictionary. it passes as a=12, b=10, and c=90.

```py
def total(a: int,b: int,c: int) -> int:
    return a + b + c
```

```py
numbers = {"a":1,"b":20,"c":90}
print(total(numbers["a"],numbers["b"],numbers["c"]))
```

<!-- unpacking -->
```py
numbers = {"a":1,"b":20,"c":90}
print(total(**number))
```

if we use default value, the list elements can be lesser than the provided args in the list, not not more than that. 
im the above example it cannot be more than 3.
if default value is not provided, the len of the list should be exactly same as len of function arguments.

# *args:

The *args syntax allows a function to accept any number of positional arguments. 
When a function parameter is preceded by *, it collects all the additional positional arguments into a tuple.

```py
def function_name(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3, "salam")

```
# **kwargs:
Similarly, **kwargs allows a function to accept any number of keyword arguments. When a function parameter is preceded by **, it collects all the additional keyword arguments into a dictionary.

```py
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="John", age=25, city="New York")
```

Combining both *args and **kwargs allows a function to accept any combination of positional and keyword arguments.

```py
def function_name(arg1, *args, kwarg1="default", **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

function_name(1, 2, 3, kwarg1="custom", name="John", age=25)
```

In this example, arg1 is a required positional argument, *args collects additional positional arguments,
 kwarg1 is a keyword argument with a default value, and **kwargs collects additional keyword arguments.


## map
apply a function on each element of an iterable

```py map(function, iterable)```

it returns a new list with the function applied to each of the elements.


```py



def yell(*args: str) -> list:
    """returns upper case of the input arguments

    Returns:
        list: upper cased words
    """
    upperCased = list()
    for word in args:
        upperCased.append(word.upper())
    print(*upperCased)


def main():
    yell("Hello hyderabad")
    
if __name__ =="__main__":
    main()
    
    
    
def yell(words):
    return words.upper()

def main():
    print(yell("Hello hyderabad"))
    
if __name__ =="__main__":
    main()

```

### List Comprehension

List comprehension is a concise way to create lists in Python. It provides a compact syntax for creating a list by specifying the elements you want to include,

along with optional conditions to filter those elements. 

IT RETURNS A LIST WITH EACH CONTAINING EACH ELEMENT OF THE ITERABLE.



### Dictionary Comprehension

it returns a dictionary.

```py
{key_expression: value_expression for item in iterable if condition}
```
key_expression: The expression for the dictionary keys.
value_expression: The expression for the corresponding dictionary values.
item: The variable representing each element in the iterable.
iterable: The sequence of elements (e.g., list, tuple, string) to iterate over.
condition: (optional) A filter that determines whether the item should be included in the dictionary.



```py
subjects = ["Mathematics","Physics","Logic","Biology"]

new_subjects = [{"name":subject,"core":"Artificial Intelligence"} for subject in subjects]
print(new_subjects)

```



## Filter

the filter function is a built-in function that is used to filter elements of an iterable (such as a list) based on a given function, called a predicate.
The filter function returns an iterator that contains only the elements for which the predicate function returns True.

```py
filter(function, iterable)
```




## Generators

```py
def main():
    n = int(input("How many times you want to see the person laugh: "))
    laughBox = laugh(n)
    for happyFace in laughBox:
        print(happyFace)
    
    
# if the inputs gets bigger and bigger, our computer memory would not able to handle it, because the laugh function returns all the outputs at once.
def laugh(n):
    box = []
    for i in range(n):
        box.append("😂"*i)
        
    return box

if __name__ == "__main__":
    main()
    
```

