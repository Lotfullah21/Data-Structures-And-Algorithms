class Solution:
    def greaterThanX(self,arr,n,x):
        #return required result
        #code here
        count = 0
        for ele in arr:
            if ele>x:
                count+=1
        return count