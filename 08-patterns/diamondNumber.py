""" 
    1  
  2 3 2  
3 4 5 4 3  
  2 3 2  
    1
"""
# Homework

n = int(input(""))
num_space = n//2
digit = 1
num_stars = 1

for row in range(1, n+1):  
    for i in range(1, num_space + 1):
        print("*", end=" ")
    
    if (row<=n//2+1):
        digit = row
    else:
        digit = n - row + 1
        
    for j in range(1,num_stars + 1):
        print(digit, end=" ")
        
        if (j<num_stars//2+1):
            digit = digit + 1
        else:
            digit = digit - 1
    for i in range(1, num_space + 1):
        print("*", end=" ")
    print()
    
    if (row<=n//2):
        num_space = num_space -1 
        num_stars = num_stars + 2
    else:
        num_stars = num_stars - 2
        num_space = num_space + 1