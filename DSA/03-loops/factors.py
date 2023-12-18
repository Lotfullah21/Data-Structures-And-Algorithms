n = int(input(""))
count = 0
print("numbers that are factor of",n,"ara : ",end=" ")
for i in range(1,n+1):
    if n%i==0:
        count = count + 1
        print(i,end=" ")
print("\ntotal numbers that are factors of",n,"are = ",count)