# Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.

# using set, it is possible to have same index for a and b.


"""
for instance, 
k = 4
a = [1,4,2,4]

a = 1
b = 3
is b in set? No

a = 4
b = 0
is b in set? No

a = 2
b = 2
is b in set? Yes.
return true.
but we can see the occurrence is one and we are adding same number to get k.


"""



def main():
    n , k = map(int,(input().split(" ")))
    arr = list(map(int, input().split()))
    answer = pairSum(arr, k)
    if answer:
        print("Y")
    else:
        print("N")
    
    
def pairSum(arr,k):
    my_set = set()
    for i in range(0, len(arr)):
        my_set.add((arr[i],i))
            
    for i in range(len(arr)):
        a = arr[i]
        b = k - a
        if b in my_set:
            return b[i], i
    return False
    
    
if __name__ == "__main__":
    main()