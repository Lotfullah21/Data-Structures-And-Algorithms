# Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.


def main():
    n , k = map(int,(input().split(" ")))
    arr = list(map(int, input().split()))
    answer = pairSum(arr, k)
    if answer:
        print("Y")
    else:
        print("N")
    
    
def pairSum(arr,k):
    my_dict = {}
    for i in range(0, len(arr)):
        if arr[i] in my_dict:
            my_dict[arr[i]] = my_dict[arr[i]] + 1
        else:
            my_dict[arr[i]] = 1
            
    for ele in arr:
        a = ele
        b = k - a
        if (a!=b and b in my_dict):
            return True
        elif (a==b and my_dict[b]>1):
            return True
    return False
    
    
if __name__ == "__main__":
    main()