class Solution:
    def maxPairAnd(self,arr: list) -> list:
        n = len(arr)
        # Find the most significant bit from left to right.
        for i in range(31, -1, -1):
            count = 0
            for j in range(n):
                if self.checkBit(arr[j], i)==True:
                    count+=1
            # If count of element which have set bit is >=2, remove them or fill it with zero, we need only two to compare.
            if count>=2:
                for j in range(n):
                    if self.checkBit(arr[j], i)== False:
                        arr[j]=0
        print(arr)
        idx1 = -1
        idx2 = -1
        # From the remaining elements which their values did not become zero, choose two elements and do bitwise and operation.
        for i in range(n):
            if arr[i]>0 and idx1 ==-1:
                idx1 = i
            elif arr[i]>0 and idx1!=-1:
                idx2 = i
                break
        return arr[idx1]&arr[idx2]
    # To find the set bit, do the bitwise and operation.
    def checkBit(self, N, i):
        if N&(1<<i)!=0:
            return True
        else:
            return False
        
solution = Solution()
arr = [4, 8, 12, 16]
result = solution.maxPairAnd(arr)
print(result)