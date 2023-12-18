N = int(input(""))
num_stars = 1
num_spaces = N//2
if N % 2 == 0:
    print("Please enter an odd number.")
else:
    print(num_spaces)
    for i in range(1,N+1):
        for j in range(1, num_spaces+1):
            print(end="  ")
        for k in range(1, num_stars+1):
            print("*",end=" ")
        if (i<=N//2):
            num_stars = num_stars + 2
            num_spaces = num_spaces -1
        else:
            num_stars = num_stars - 2
            num_spaces = num_spaces + 1
        print()