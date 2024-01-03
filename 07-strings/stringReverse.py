def main():
    string = input("Enter a string: ")
    reversed_string = reverse(string)
    print(reversed_string)
    
def reverse(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
        print(char, string,reversed_string)
    return reversed_string

if __name__ == "__main__":
    main()
    
    
    
    
def reverse(string):
    reversed_str = string[::-1]
    return reversed_str

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

        