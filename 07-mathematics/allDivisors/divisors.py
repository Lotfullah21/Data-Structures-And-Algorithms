import math
def divisors(n: int) -> list[int]:
    "returns divisors of integer n"
    divisors = []
    i = 10000
    while i<(math.sqrt(n)):
        if n%i==0:
            divisors.append(i)
        i+=1
    # Now variable i increased from 1 to some larger number.
    while i>=1:
        if n%i==0:
            divisors.append(n//i)
        i = i - 1
    return divisors
 
 
n = int(input("Enter an integer: "))    
result = divisors(n)
print("all divisors of",n,"are =",result)