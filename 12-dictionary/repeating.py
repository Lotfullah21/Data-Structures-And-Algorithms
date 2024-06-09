"""
given an array, find the first Occurrence of a number.

Idea: for the given number, generate a dictionary where the key is the number itself, and value is the count of that number:
check for the count, if count is 1 return -1.


"""


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = nonRepeatingNumber(arr)
    print('result',result)
    

def nonRepeatingNumber(arr):
    my_count_dict = {}
    for num in arr:
        if num in my_count_dict:
            my_count_dict[num] = my_count_dict[num] + 1
        else:
            my_count_dict[num] =  1
            
    print(my_count_dict)
    for x in arr:
        if my_count_dict[x]==1:
            return x
    return -1
        
 

if __name__ == "__main__":
    main()