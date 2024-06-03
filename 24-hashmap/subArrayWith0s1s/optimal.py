#User function Template for python3
class Solution:
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        freq = {0:1}
        ans=0
        prefixCountOf0 = self.prefixSum(arr, 0)
        prefixCountOf1 = self.prefixSum(arr, 1)
        for endPoint in range(len(arr)):
            diff = prefixCountOf1[endPoint]-prefixCountOf0[endPoint]
            if diff in freq:
                ans = ans + freq[diff]
                # Increment the count of the given difference with 1.
                freq[diff] = freq[diff]+1
            # If diff is not in the freq map, add it to map, it might be one starting point potential.
            if diff not in freq:
                 freq[diff] = 1
                 
        return ans

    def prefixSum(self,arr,num):
        "Returns a new array containing prefix count of a given number (num)"
        pf = [0]*len(arr)
        c=0
        for i in range(len(arr)):
            if arr[i]==num:
                c+=1
            pf[i]=c
        return pf
    

arr= [1 ,0 ,0 ,1 ,0 ,1 ,1]
soluion = Solution()
res = soluion.countSubarrWithEqualZeroAndOne(arr, len(arr))
print("Number of sub arrays that has equal number of ones and zeros =",res)