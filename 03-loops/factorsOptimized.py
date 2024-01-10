# if a digit is a factor, it means there should be another number as well
# lets say, fact1 * fact2 = Number
# suppose N = 12, what are the numbers that if we multiply, it results to 12. 1*12, 2*6, 3*4, 12*1.
# fact2 = Number/fact1
# fact1 fact2 = (N/fact1)
# 1 ------ 12/1 = 12
# 2 ------ 12/2 = 6
# 3 ------ 12/3 = 4
# --- Breaking point --- 
# 4 ------ 12/4 = 3
# 6 ------ 12/2 = 6
# 12 ------ 12/12 = 1

# we can see after fact1>fact2(N//fact1), the pattern is the same,
# fact1 < N/fact1 => fact1*fact1<n = fact1 = (n)**0.5



n = int(input("Enter a value: "))
factors = []
count = 0
# here as it goes only to the half of the way, we are not able to see the factor numbers, but count will be correct.

for i in range(1, int(n**0.5) +1 ):
    # check if the number is divisible by i
    if n % i == 0:
        factors.append(i)
        # check if the factor (iteration number) is not equal n//i, because if it is there, it means we are having same digit and it should not be counted twice
        if i != n // i:
            factors.append(n//i)
            count += 2
        # if factor and int part of division is equal, add only one to the count variable
        else:
            count += 1
  
   
print("factors",sorted(factors))            
print("count",count)
