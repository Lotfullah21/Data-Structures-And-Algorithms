"""
You are given an array arr(0-based indexing). The size of the array is given by n. You need to update an element at the given index. The arr[i] of the array is initially set to i+1.

Input:
n = 4
index = 1,element = 10
Explanation: Element at 1st index updated to 10

"""
def updateArray(arr,n,idx,element):
    arr[idx] = element
