

n = int(input("How many you rows you want to print: "))

for row in range(n+1):
    # rows controls how many times the inner loops should run.
    for col in range(1, row+1):
        print("*",end="")
    # after each iteration of inner loop, print a new line. 
    print()
    
