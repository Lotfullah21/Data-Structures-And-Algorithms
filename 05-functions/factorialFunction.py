
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        
    return fact
    
n = int(input("Enter the N "))    
r = int(input("Enter the R "))   

fact = factorial(n)
fact_r = factorial(r)
fact_nr = factorial(n-r)

answer = fact/(fact_nr * fact_r)
print("factorial n = ",fact)
print("factorial r = ",fact_r)
print("factorial n-r = ",fact_nr)
print("ncr = ",answer)