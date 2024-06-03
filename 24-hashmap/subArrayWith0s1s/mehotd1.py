#User function Template for python3
class Solution:
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        freq = {0:1}
        ans = 0
        k=0
        # Replace the index with the element equal to zero to -1.
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=-1
        # Calculate prefix for the new array.
        pf = self.prefixSum(arr)
        for end in range(len(arr)):
            # pf[end]-pf[s-1] = k //0
            diff = pf[end]-k
            if diff in freq:
                ans+=freq[diff]
            if pf[end] not in freq:
                freq[pf[end]]=1
            else:
                freq[pf[end]] += 1
        return ans
            
    # Function to get prefix sum of an array.
    def prefixSum(self,arr):
        pf = [0]*len(arr)
        for i in range(len(arr)):
            pf[i] = pf[i-1]+arr[i]
        return pf
    


    
arr = [1,0,0,-1,1,-1,1]
arr= [1 ,0 ,0 ,1 ,0 ,1 ,1]
soluion = Solution()
res = soluion.countSubarrWithEqualZeroAndOne(arr, len(arr))
print("Number of sub arrays that has equal number of ones and zeros =",res)