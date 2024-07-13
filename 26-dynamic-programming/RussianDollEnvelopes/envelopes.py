class Solution:
    class Pair:
        def __init__(self, w, h):
            self.w = w
            self.h = h
            
        def __repr__(self):
            return f"Pair(w={self.w}, h={self.h})"
        def __lt__(self, other):
            if self.w!=other.w:
                if self.w<other.w:
                    return True
                # else:
                #     return False
            else:
                if self.h>other.h:
                    return True
                # else:
                #     return False
        
        
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        arr = []
        for i in range(n):
            arr.append(self.Pair(envelopes[i][0], envelopes[i][1]))
        print("Before sorting:", arr)
        arr.sort()
        print("After sorting:", arr)
        ans = 0
        dp = [0]*n
        for i in range(n):
            low = 0
            high = ans
            while low<high:
                mid = (low+high)//2
                if arr[i].h>dp[mid]:
                    low = mid+1
                else:
                    high = mid
            dp[low] = arr[i].h
            if ans==low:
                ans+=1
        return ans
if __name__ == "__main__":
    envs = [[3, 9], [2,7],[2,7], [3,9]]
    solution = Solution()
    res = solution.maxEnvelopes(envs)
    print("Max Envelopes:", res)