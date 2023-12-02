N = int(input(""))

# identify the pattern and see how the individual elements are changing from line to line
# initialize the elements to be appear in the first row 
# after for loops, add on how the elements should be changed

num_stars = N//2 + 1
num_spaces = 1

for i in range(1,N+1):
    for j in range(1, num_stars+1):
        print("*",end=" ")
    for k in range(1, num_spaces+1):
        print("-",end=" ")
    for l in range(1, num_stars + 1):
        print("*",end=" ")
    if (i<=N//2):
        num_stars = num_stars -1
        num_spaces = num_spaces +2
    else:
        num_stars = num_stars + 1
        num_spaces = num_spaces - 2
    print()
    

