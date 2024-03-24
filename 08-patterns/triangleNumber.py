# N  = int(input(""))

# inc = 0
# num = 1

# for i in range(1, N+1):
#     for j in range(1,num+1):
#         print(inc + j, end = " ")
#     num = num + 1
#     inc = inc + 1
#     print()




N  = int(input(""))
val = 1
num = 1
for i in range(1, N+1):
    for j in range(1,num+1):
        print(val,end=" ")
        val = val + 1
    # controlling what to be printed in each column.
    num = num + 1
    print()
