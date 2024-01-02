rows = 4
cols = 20

array = []

for i in range(rows):
    # for each row, add columns with the element 1 as it is initial value.
    # 20*[1] means 20 elements filled with 1.
    array.append([1]*cols)
# when we use len method, it counts number of rows;
# when we use len(arr[0]), we count number of columns, Logically it means how many elements are there in first row.
print(len(array[0]))    

print(array)
