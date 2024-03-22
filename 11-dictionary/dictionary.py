# dictionary allow us to use one data structure and have addresses or indexes which are not necessary to be integers

my_dict  = {}
capitals = {"Afg":"Kabul","Ind":"Delhi","Iran":"Tehran"}
print("countries",capitals)
for capital in capitals:
    print(capital)
    
# adding to a dictionary; remember to have unique keys.
capitals["Tajikistan"] = "Dushenbah"
print(capitals)

# using .keys() and .values() to retrieve values and keys.
print("Keys =",capitals.keys())
print("Values =",capitals.values())

# iterating over values
for x in capitals.values():
    print(x)
    

for w in capitals:
    print("w",w)