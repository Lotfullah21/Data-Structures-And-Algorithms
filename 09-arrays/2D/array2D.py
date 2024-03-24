n = int(input("How many rows? "))
m = int(input("How many columns? "))
array = []
for i in range(n):
    # Create a 1D array, with m elements filed with zeros.
    array.append([0]*m)
    for j in range(m):  
        # Assign to each index of the array a value.
        print("row",i,"column",j)
        array[i][j] = int(input(""))
        
print()
print("Using nested loop to go deeper and get the elements using its columns and rows indices.")
for i in range(n):
    for j in range(m):  
        # print each element until we reach m
        print(array[i][j],end=" ")
    # Exit the loop and print a new line when have reached to the end of row.
    print()
    
print("Using a single loop, it goes for each index of the array and print its elements.") 
for i in range(n):
    print(array[i])
