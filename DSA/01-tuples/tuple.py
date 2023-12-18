# initialize a tuple


new_tuple = ()
print(type(new_tuple),new_tuple)

tuple_1 = (1, 2, 3)
print("tuple_1 =",tuple_1)

tuple_mixed = (1,2,"hello","salam")
print("tuple mixed =",tuple_mixed)

tuple_concatenate = tuple_1 + tuple_mixed
print("tuple_concatenate =",tuple_concatenate)

# error, we cannot mutate tuples
# tuple_concatenate[0] = 10 //  error
