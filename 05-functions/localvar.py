x = 12
def total(t):   
    """add the input value to 2 and save bind to w.

    Args:
        t (int): an int value that adds to two.
    """
    w = x +  2
    print(w)
    
x = 90
print(total(12))




## Error
# x = 12
# def total(t):   
#     # it gives an error, because we are trying to modify a global variable.
#     x = x +  2
#     print(x)  
# print(total(12))