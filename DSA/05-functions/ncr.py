N = int(input("Enter N "))
r = int(input("Enter r "))

fact = 1
for i in range(1, N + 1):
    fact = fact * i
    
factr = 1
for i in range(1, r + 1):
    factr = factr * i     

factnr = 1
for i in range(1, (N-r) + 1):
    factnr = factnr * i

print("fact = ",fact, "fact r = ",factr,"fact n-r = ",factnr)



ans = (fact)//((factr)*(factnr))

print(ans)