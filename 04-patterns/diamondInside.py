'''
Pattern for n = 5.
*** ***  
**   **  
*     *  
**   **  
*** ***  
'''

# Look at how many rows are there
# initialize two variables for type of elements you are going to print
# identify number of each element in first row
# detect the pattern and change the variables.

N = int(input(""))
num_space = 1
num_stars = N//2 + 1
if N % 2 == 0:
    print("Please enter an odd number.")
else:
    for i in range(1,N+1):
        for j in range(1, num_stars+1):
            print("*",end="")
        for k in range(1, num_space+1):
            print(" ",end="")
        for k in range(1, num_stars+1):
            print("*",end="")
        print()
        if (i<=N//2):
            num_stars = num_stars - 1
            num_space = num_space + 2
        else:
            num_stars = num_stars + 1
            num_space = num_space - 2