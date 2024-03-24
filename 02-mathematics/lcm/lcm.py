def lowestCommonMultiplier(a, b):
    lcm = max(a, b)
    while True:
        if lcm%a ==0 and lcm%b==0:
            return lcm
        else:
            lcm = lcm + 1

    
    
a, b = list(map(int, input("Enter a and b: ").split()))
lcm = lowestCommonMultiplier(a, b)
print(f"the least common multiplier between {a} and {b} is = {lcm}")