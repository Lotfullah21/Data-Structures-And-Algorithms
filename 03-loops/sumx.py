sum = 0
# using list to keep the track of the inputs entered by user.
new_list = []

while True:
    n = input("Enter a number (or 'x' to exit): ")
    if n == 'x':
        break
    new_list.append(int(n))
    sum += int(n)

print("Sum of entered numbers:", sum)




# first solution.

# sum = 0
# x = True
# n = input("Enter a number or x to exit: ")
# new_list = list()
# while n!="x":
#     new_list.append(int(n))
#     sum = sum + int(n)
#     n = input("Enter a number or x to exit! ")

# print(sum)