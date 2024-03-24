subjects = [
    {"name":"Artificial Intelligence","duration":"4 months"},
    {"name":"Deep learning","duration":"4 months"},
    {"name":"Machine learning","duration":"3 months"},
    {"name":"Mathematics","duration":"6 months"},
    {"name":"Machine learning","duration":"3 months"},
    {"name":"Mathematics","duration":"6 months"},
    {"name":"Programming","duration":"4 months"}
    ]

new_subjects = set()
count = 0
for subject in subjects:
    # we can use set without checking whether the element exist or not to add elements without duplicates in the empty set.
    new_subjects.add(subject["name"])
         
print(count)
for subject in new_subjects:
    print(subject)
        
# set 
new_set = {1, 2 ,2 ,3 }
# it will give us a tuple
x = (1,2 ,2,3 ,4 )
print(type(new_set))
print(new_set)
print(type(x))
# initializing a set using set key
y = set()
print(y, type(y))
# check the size size of set, it gives us the number of uniques elements in there.
print(len(new_set))

