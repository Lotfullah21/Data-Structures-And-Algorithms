# lists are mutable, it means the elements inside a list can be changed, but the variable name still points to the same variable

fruits = ["apple","banana","grapes","orange"]

print("before mutation",fruits)


fruits[0] = "peach"
print("after mutation",fruits)