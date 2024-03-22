# append mutates and add an element to the end of the list

fruits = ["apple","banana","grapes","orange"]
fruits.append("eggs")

print(fruits)

fruits.append(["red","blue"])
print(fruits)


# extend add the elements to the end of an array

fruits.extend(["red","green"])
print(fruits)


# delete a specific element from the list.
fruits.remove("red")
print(fruits)

# delete the from index 2.
del(fruits[2])
print(fruits)

# pop method removes an element from the end of the list
fruits.pop()
print(fruits)