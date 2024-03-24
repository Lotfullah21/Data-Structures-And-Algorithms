def total(a: int,b: int,c: int=20) -> int:
    return a + b + c

# if we use default value, the list elements can be lesser than the provided args in the list, not not more than that. 
# im the above example it cannot be more than 3.

# if default value is not provided, the len of the list should be exactly same as len of function arguments.

numbers = [12,12]
print(total(*numbers))



# if we pass it as a dictionary.
def new_total(a,b,c):
    return a + b + c

new_numbers = {"a":1,"b":20,"c":90}
print(new_total(**new_numbers))