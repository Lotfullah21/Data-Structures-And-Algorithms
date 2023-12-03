n = int(input("Enter a number: "))
root = 0
inc = 0.001

# i = 0
# while(i*i<=n):
#     root = i 
#     i+=1
# print(root)


for i in range(1, int((n)**0.5)+ 1):
    if i * i > n:
        break
    else:
        root = i
        i+=inc
print(root)