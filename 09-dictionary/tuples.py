empty_tuple = ()
print(empty_tuple)

# tuples with one value
single_e_tuple = (2,)
print("single tuple =", single_e_tuple)
# without comma, python will not take this one as a tuple
x = (2)
print("x =", x)

# indexing: it gives us a single value
tuples = (1, 2, 3, "hello")
print("tuples =", tuples)

print("value at index position =", tuples[3])
print("last element =", tuples[-1])

# Slicing: it gives us a tuple
print("elements up to index 2 =", tuples[0:2])
print("elements up to last index", tuples[0:-1])
print("all elements =", tuples[0:])

# contatenation: adding two tuples together
t_1 = (1, 2, 3, 4, 5)
t_2 = ("salam", "Hello", "Bonjur", "Namasti")
cn = t_1 + t_2
print("t_1 + t_2 =", cn)

# Swap values
x = 10
y = 3
print("x =", x, "y =", y)
# 1. create a temporarily variable or place holder, and put the value of x in it.
temp = x
# 2. x is empty now, put the value of y in it
x = y
# 3. y is empty now, put the value of x which was assigned to temporarily variable into y
y = temp
print("after swaping values", "x =", x, "y =", y)

# this can be done easily using tuples
x = 10
y = 3
x, y = y, x
print("using tuples ", x, y)


# Looking for an element
q = (2, 3, ("ML", "AI", 0), 'salam')
print(len(q))
print(2 in q)
print("salam" in q)
# check if "ML" is in q, it would false, bcz here we are looking to each element as single object
# which meas ("ML", "AI", 0) all are single object
print("ML" in q)
print(0 in q)
