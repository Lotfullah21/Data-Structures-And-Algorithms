x = 12

def total(t):
    global x
    for i in range(t):
        x = x + 2
    print(x)

total(3)

print(x)