# we can use indexing and iterate over the list elements.


# list of colors
colors = ["red","blue","green"]

for i in range(len(colors)):
    print(colors[i])

# cleaner way
for color in colors:
    print(color)

# list of numbers
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)


# list of countries
countries = ["Afg","Ind","Iran"]
for country in countries:
    print(country)
    
for country in range(len(countries)):
    print(countries[country])

# mixed information 
mixed_data = ["Afg",1,2,"red","green"]
for data in mixed_data:
    # iterate through the list as long as their is an element and each time, print mix_data.
    print(mixed_data)
    
    
    