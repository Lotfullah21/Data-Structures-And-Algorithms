n = int(input("How many rows do you want: "))

num = 1
for row in range(1,n+1):
    # start from 1 till number of rows in the outer loop in each iteration.
    for col in range(1, row + 1):
        print(num,end=" ")
        num = num + 1
    print()
