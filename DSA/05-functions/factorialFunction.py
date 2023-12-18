
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        
    return fact
    
n = int(input("Enter the N "))    
r = int(input("Enter the R "))   

fact = factorial(n)
factr = factorial(r)
factnr = factorial(n-r)

answer = fact/(factnr * factr)
print("factorial n = ",fact)
print("factorial r = ",factr)
print("factorial n-r = ",factnr)
print("ncr = ",answer)