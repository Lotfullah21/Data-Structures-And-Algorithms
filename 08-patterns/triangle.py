
'''
*
**
***
****
*****

'''
# as we can see from the above pattern, number of stars is increasing by one in each row.



numStars = 1
n = int(input(""))
for i in range(1, n+1):
    for j in range(1, numStars+1):
        print("*",end = " ")
    # increment number of stars here, this controls how many elements or how many times the inner loop should run
    numStars = numStars + 1
    # to add a new line after each execution
    print()



