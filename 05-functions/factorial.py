fact = 1

# the idea behind finding factorial of a number is multiplying sequential number from beginning until the end of that number starting from 1.
N = int(input(""))
for i in range(1,N+1):
    fact = fact * i
print(fact)