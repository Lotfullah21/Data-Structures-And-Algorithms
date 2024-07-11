def find_max_numbers(a, b, c):
    if a >= b and a >= c:
        firstMax = a
        if b >= c:
            secondMax = b
            thirdMax = c
        else:
            secondMax = c
            thirdMax = b
    elif b >= a and b >= c:
        firstMax = b
        if a >= c:
            secondMax = a
            thirdMax = c
        else:
            secondMax = c
            thirdMax = a
    else:
        firstMax = c
        if a >= b:
            secondMax = a
            thirdMax = b
        else:
            secondMax = b
            thirdMax = a
    
    return firstMax, secondMax, thirdMax

# Example usage:
a, b, c = 5, 3, 7
firstMax, secondMax, thirdMax = find_max_numbers(a, b, c)
print("First Max:", firstMax)
print("Second Max:", secondMax)
print("Third Max:", thirdMax)
