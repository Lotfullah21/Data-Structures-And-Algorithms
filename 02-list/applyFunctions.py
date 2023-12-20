def square(x):
    return x**2

def sqrt(x):
    return x**0.5

applied_list = []

def applyToEach(fnList,x):
    for f in fnList:
        for el in x:
            el = f(el)
            applied_list.append(el)
            print(el)
        print()    
    return applied_list
applied = applyToEach([square,sqrt],[12,2,2,22])
print(applied)