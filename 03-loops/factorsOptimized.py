n = int(input("Enter a value: "))
factors = []
count = 0

# here as it goes only to the half of the way, we are not able to see the factor numbers, but count will be correct.

for i in range(1, int(n**0.5) +1):
    # check if the number is divisible by i
    if n % i == 0:
        factors.append(i)
        print(i)
        # check if the factor (iteration number) is not equal n//1, because if it is there, it means we are having same digit and it should not be counted twice
        if i != n // i:
            factors.append(n//i)
            count += 2
        # if factor and int part of division is equal, add only one to the count variable
        else:
            count += 1
print("factors",sorted(factors))            
print("count",count)
