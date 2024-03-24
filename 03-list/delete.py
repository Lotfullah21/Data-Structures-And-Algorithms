"""
You are given an array arr(0-based indexing). The size of the array is given by n. You need to delete an element at given index and print the modified array. The arr[i] of array is initially set to i+1.
Deletion means you need to shift all the elements after that index to the left by 1 position and set the last element as zero.


Input:
n = 6
index = 3
# remove the element from index 3.
original array = [1 2 3 4 5 6]
Output: 1 2 3 5 6 0

"""

def deleteFromArray(arr,n,idx):
    del arr[idx]
    arr.append(0)
    return arr
