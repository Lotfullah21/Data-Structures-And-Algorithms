# n = int(input(""))
n = 102
count = 0
for i in range(1, n+1):
    if(n%i==0):
        count = count + 1


if count==2:
    print("Primer number")
else:
    print("Not prime number")