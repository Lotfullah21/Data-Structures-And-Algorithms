def main():
    string = input("Enter a string to toggle: ")
    toggled_string = toggle(string)
    print(toggled_string)
    
def toggle(arr):
    toggled_strings_array = []
    for i in range(0,len(arr)):
        if (ord(arr[i])>=65 and ord(arr[i])<=90):
            toggled_strings_array.append(chr(ord(arr[i])+32))
        else:
            toggled_strings_array.append(chr(ord(arr[i])-32))            
    return "".join(toggled_strings_array)
if __name__ == "__main__":
    main()




# 2nd solution

# def toggle(arr):
#     toggled_chars = []
#     for char in arr:
#         if 'A' <= char <= 'Z':
#             toggled_chars.append(chr(ord(char) + 32))
#         elif 'a' <= char <= 'z':
#             toggled_chars.append(chr(ord(char) - 32))
#         else:
#             toggled_chars.append(char)
#     return ''.join(toggled_chars)


# 3rd solution

# def toggle(arr):
#     for i in range(len(arr)):
#         if 'A' <= arr[i] <= 'Z':
#             arr[i] = arr[i].lower()
#         elif 'a' <= arr[i] <= 'z':
#             arr[i] = arr[i].upper()
