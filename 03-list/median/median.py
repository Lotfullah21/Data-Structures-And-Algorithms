"""
Given an array a[ ] of size N. The task is to find the median and mean of the array elements. 
Mean is average of the numbers and median is the element which is smaller than half of the elements and greater than remaining half.  
If there are odd elements, the median is simply the middle element in the sorted array. 
If there are even elements, then the median is floor of average of two middle numbers in the sorted array. If mean is floating point number, then we need to print floor of it.

mean(): It takes the array and its size N as parameters and returns the mean as an integer.
median(): It takes the array and its size N as parameters and returns the median as an integer, the array should be sorted from least to greatest.

"""
class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        
        A.sort()
        if N%2==0:
            # if it is even, return the avg of the middle numbers.
            avg = (A[N/2-1]+ A[N/2])/2
            return avg
        else:
            return A[N//2]
            
        ##Your code here
        #If median is fraction then convert the median to integer and return
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        total = 0
        for e in A:
            total = total + e
        return total//N