# # Normal Function
# def root(x):
#     "Takes an integer and returns square root of a number"
#     return int(x**0.5)
# print(root(81))


# # Using Lambda function.
# root = lambda x : (x)**0.5
# print(root(49))


# 2nd Function
def greet():
    return "Hello Kabul"
print(greet())

greet = lambda: "Hello Kabul From lambda"
print(greet())

# # Third Function
# square = lambda x: x**2
# print(square(9))

# # Fourth Function
# CircleArea = lambda r, pi=3.14: pi*(r)**2
# print(CircleArea(9))

# # Fifth
# # If else expression is used here instead of commands.
# factor = lambda x,y: "factor" if x%y==0 else "not factor"
# print(factor(10, 2))