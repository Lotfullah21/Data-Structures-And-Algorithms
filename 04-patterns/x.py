stars = 1
n = int(input(""))
for i in range(1, n+1):
    for j in range(1, stars + 1):
        print("*",end="  ")
    # increment stars
    stars +=2
    # add a new line
    print()
