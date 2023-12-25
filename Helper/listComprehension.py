## [expression for item in iterable ]


# add one to each element of the range tuple.
squared = [x+1 for x in range(10)]
print(squared)

# return x if x%2==0
even_numbers = [x for x in range(10) if x%2==0]
print(even_numbers)

words = ("HELLO")
lowerCased = [word.lower() for word in words]
print(lowerCased)

# join returns a string
w = "_".join(lowerCased)
print(w, type(w))

# split returns a list 
new_w = w.split("e")
print(new_w, type(new_w))


# Create a 2D matrix using nested list comprehension
matrix = [[x + y for x in range(6)] for y in range(4)]
print(matrix)