# print # n times
# for instance if n=4, ####


n = int(input("How many rows do you want:? "))

for i in range(n):
    print("0")
# if we just use print("#"), loop will run n times, and every time it starts a new line and print #.
# to have a all elements in one which are result of the loop iteration, we can add, end = "", in print function so that in each iteration it does not start a new line.

# 
for i in range(n):
    print("0",end = " ")
    
# as we can see, we cannot do much with a single loop, if having a beautiful pattern is in consideration, an inner loops also had to be used.

for i in range(n):
    for j in range(n):
        print("0", end = " ")
    print()