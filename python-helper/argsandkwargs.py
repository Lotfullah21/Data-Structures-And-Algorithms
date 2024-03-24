
# positional arguments
def total(*args):
    total = 0
    print(args)
    for arg in args:
        total = total + arg
    return total
        
        
print(total(2,2,12,21,2,1,21,21,21))


# keyword arguments
def total(**kwargs):
    total = 0
    print(kwargs)
    for key,val in kwargs.items():
        total = total + val
        print(key,"=",val)
    return f"sum = {total}"
        
        
print(total(a=10,b=100))



# keyword arguments
def mixed(*args,**kwargs):
    total = 0
    print(kwargs)
    for key,val in kwargs.items():
        total = total + val
        print(key,"=",val)
    for val in args:
        total = total + val
        print(val)
        
    return total
            
print(mixed(90,a=10,b=100))
