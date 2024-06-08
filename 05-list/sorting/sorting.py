# sort and sorted both of them sort the elements inside a list. but sort mutates the list where sorted does not mutate the original list and sort does not return anything.

nums = [1,2,3,4,43,1,2,3,6,90,0]
# mutate the nums list
sort_mutates = nums.sort()
# the below print function will return none, because the original mutation is done on nums.
print("mutated list",sort_mutates)
print("original list",nums)
# does not mutate the original list
new_nums =[99,1,7,9,2,21,0]
sort_no_mutation = sorted(new_nums)
print("sorted list",sort_no_mutation)
print("original list",new_nums)
