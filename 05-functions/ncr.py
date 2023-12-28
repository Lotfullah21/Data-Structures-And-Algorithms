N = int(input("Enter N "))
r = int(input("Enter r "))

fact = 1
for i in range(1, N + 1):
    fact = fact * i
    
fact_r = 1
for i in range(1, r + 1):
    fact_r = fact_r * i     

fact_nr = 1
for i in range(1, (N-r) + 1):
    fact_nr = fact_nr * i

print("fact = ",fact, "fact r = ",fact_r,"fact n-r = ",fact_nr)



ans = (fact)//((fact_r)*(fact_nr))

print(ans)