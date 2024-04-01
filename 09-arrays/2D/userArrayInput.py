rows = 3
cols = 4 
arr = [[0]*cols]*rows
arr[0][0] = 10
for ele in arr:
    print(ele)
    
    
arr = [[0 for j in range(cols)] for i in range(rows)]
print(arr)