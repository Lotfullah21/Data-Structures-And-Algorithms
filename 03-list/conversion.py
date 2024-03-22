# a string can be converted to a list using list()

numbers = "123456789"
print("numbers string", numbers,type(numbers))
numbers_list = list(numbers)
print("numbers lists",numbers_list,type(numbers_list))

# string.split(): to split a string into characters and converting them back to list, split can be done by the parameters we define inside split()
splitted_numbers = numbers.split("4")
print(splitted_numbers,type(splitted_numbers))

# "".join(list): it is used to convert a list characters into a string.

aplphabets_list = ["a","b","c","d","e","f"]
new_alphabets = " ".join(aplphabets_list)

print(new_alphabets,type(new_alphabets))