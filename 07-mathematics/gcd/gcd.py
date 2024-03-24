def greatestCommonFactor(a, b):
    while a!=b:
        if a>b:
            a = a - b
        else:
            b = b - a
    return a
    
a, b = list(map(int, input("Enter a and b: ").split()))

gcd = greatestCommonFactor(a, b)
print(f"greatest common factor between {a} and {b} is = {gcd}")