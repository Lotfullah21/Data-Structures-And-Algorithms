list_1 = [1,2,3,4,5]
list_2 = [2,1,1,23,3,5]


# due to the fact that we are mutating the list_1, for 0th index it will check, but the indexing would be difficult.
list_temp = list_1[:]


for ele in list_temp:
    if ele in list_2:
        list_1.remove(ele)
        
print(list_1)

