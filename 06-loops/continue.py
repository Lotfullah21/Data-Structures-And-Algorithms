n = int(input(""))

for i in range(1,n + 1):
    # the moment i becomes 2, it will skip execution after the continue statement and start again from for loop
    if (i==2):
        continue
    # the moment it becomes 10, it will break of the loop and will not execute any statement after the break statement.
    elif (i==10):
        break
    print(i)