def main():
    input_str = input("Enter a string: ")
    # input_str = input("Enter a string: ").lower()
    n = len(input_str)
    arr = [0] * n
    for i in range(n):
        if input_str[i].isupper():
            arr[i] = input_str[i].lower()
        else:
            arr[i] = input_str[i]
    result = isPalindrome(input_str)
    print(result)
    
    
    
    
    
def isPalindrome(input_str):
    starting_point = 0
    ending_point = len(input_str) - 1
    while(starting_point<ending_point):
        
        if (input_str[starting_point]==input_str[ending_point]):
            print("start",starting_point,"ending_point",ending_point)
            starting_point = starting_point + 1
            ending_point = ending_point - 1
            return True
     
        else:
            return False

    
if __name__ == "__main__":
    main()