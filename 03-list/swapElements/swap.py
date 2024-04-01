def swap(a: int, b:int) -> int:
    "Swaps the references of abject a and b"
    temp = a
    a = b
    b = temp
    return a, b
    
    
a = 10
b = 12
print("a and b before swapping","a=", a, "b=",b)
a, b = swap(a, b)
print("a and b after swapping","a=" ,a,"b=", b)