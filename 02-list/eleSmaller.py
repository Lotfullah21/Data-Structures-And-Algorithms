#User function Template for python3
"""
Given an unsorted array arr[] of size N containing non-negative integers. 
You will also be given an integer X, the task is to count the number of elements which are strictly smaller than X. 
The given integer may or not be present in the array given.

Input:
N = 6
arr[] = {2 2 2 2 2 2}
X = 3
Output: 6
Explanation: Here X = 3, and elements that
are smaller than X are 2 2 2 2 2 2.

"""


class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        count = 0
        for ele in arr:
            if ele<x:
                count +=1
        return count
                
        #code here
        
source = "https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/list-basic-python/problem/count-smaller-than-x"