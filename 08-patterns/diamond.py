n = int(input(""))
num_stars = 1
num_space = n//2

if n%2==0:
    print("Enter an odd number")
else:
    for i in range(1, n+1):      
        for j in range(1, num_space+1):
            print(" ",end="")
        for k in range(1, num_stars+1, 1):
            print("*",end = "")
        print()
        if (i<=n//2):
            num_space = num_space - 1
            num_stars = num_stars + 2
        else:
            num_space = num_space + 1
            num_stars = num_stars - 2