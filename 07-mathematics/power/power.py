def power(x, n):
    """
    Returns base to the power n
    """
    if n ==0:
        return 1
    temp = power(x, n//2)
    temp = temp * temp
    if n%2==0:
        return temp
    else:
        return temp * x

 
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = power(base, exp)
print(f"{base} to the power {exp} = {result}")
    