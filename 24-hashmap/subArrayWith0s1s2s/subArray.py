class Solution:
    def getSubstringWithEqual012(self, Str):
        freq = {"0@0": 1}
        ans = 0
        pfc0 = self.prefix(Str, '0')
        pfc1 = self.prefix(Str, '1')
        pfc2 = self.prefix(Str, '2')
        for endPoint in range(len(Str)):
            diff1 = pfc0[endPoint] - pfc1[endPoint]
            diff2 = pfc0[endPoint] - pfc2[endPoint]
            diff = "{}@{}".format(diff1, diff2)
            if diff in freq:
                ans += freq[diff]
                freq[diff] += 1
            else:
                freq[diff] = 1
        return ans
    
    def prefix(self, arr, num):
        pf = [0] * len(arr)
        count = 0
        for i in range(len(arr)):
            if arr[i] == num:
                count += 1
            pf[i] = count
        return pf