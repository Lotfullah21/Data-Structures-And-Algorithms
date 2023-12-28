## Function

a function is a reusable piece of code that allows us save time and memory.
by writing a function we can re-use it as many as we want.

```py

def function_name(parameter1):

    body of the function


```

a function have a

1. name
2. docstring(optional)
3. arguments(parameters)
4. a body

to use a function, we have to call(invoke) it

### difference between print() function and return expression

print() function is just a side effect, it show us the result of a computation or something that we want to see.
return expression returns result of a computation from a function, if later we use that function directly we have access to that computation result.

```py

def total(number1: int, number2: int) ->int:
    summation = number1 + number2
    print(summation)

total(12,12) # 24
answer = total(12, 12)
print(answer) # 24, undefined
new_question  = 12 + answer # undefined output as the function does not return anything, when a function does not return anything, it returns undefined.
```

```py

def total(number1: int, number2: int) ->int:
    summation = number1 + number2
    print(summation)

answer = total(12, 12)
print(answer) // 24
new_question  = 12 + answer // 36

```

we can access to the variables that defined outside the function, but we cannot modify it.

```py
12
def square(x):
    x = 1
    x = x + 1
    return x
square(12)
print(x) # 12 not 13.
```

```py
x = 12

def total(t):
    global x
    for i in range(t):
        x = x + 2
    print(x)

total(3)


```
