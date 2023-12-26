n = int(input("How many rows do you want: "))


for row in range(1, n + 1):
    for col in range(n):
        print("*", end=" ")
    n = n - 1 
    print()

