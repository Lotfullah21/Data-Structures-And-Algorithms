x = 12

# if we want to change the global variable, we have to use global keyword.

def total(t):
    global x
    for i in range(t):
        x = x + 2
    print(x)
total(3)
print(x)