# x = [[] for i in range(10)]
# x[0] = [2, 1]
# h = 0

# for i, e in enumerate(x[h]):
#     if e == 2:
#         print("e")

# print(len(x[0]))


x = [[(2,3),("jh",32)]]
for idx, ele in x[0]:
    if idx == 2:
        print(ele)
        
        
x = [[(2,3),("jh",32)]]
for idx, ele in enumerate(x[0]):
    print(idx, ele)