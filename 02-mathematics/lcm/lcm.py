def lowestCommonMultiplier(a, b, c):
    lcm = max(a, b, c)
    while True:
        if lcm%a ==0 and lcm%b==0 and lcm%c==0:
            return lcm
        else:
            lcm = lcm + 1

    
    
a, b, c= list(map(int, input("Enter a and b: ").split()))
lcm = lowestCommonMultiplier(a, b, c)
print(f"the least common multiplier between {a} and {b} is = {lcm}")