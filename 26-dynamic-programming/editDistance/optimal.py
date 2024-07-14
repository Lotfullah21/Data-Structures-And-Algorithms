class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        memo = []
        for i in range(n+1):
            row = []
            for j in range(m+1):
                row.append(-1)
            memo.append(row)
        return self.helper(word1, n-1,word2, m-1, memo)
    def helper(self, s1, i, s2, j, dp):
        # If both strings are finished, no work to be done.
        if i==-1 and j==-1:
            return 0
        if i!=-1 and j==-1:
            return i+1
        # If i is still go elements, means we need to len(s1) opeartions to make it equall to s2
        if i==-1 and j!=-1:
            return j+1
        # If answer already there, do not computet again
        if dp[i][j]!=-1:
            return dp[i][j]
        # If the characters are the same, move both indices
        if s1[i]==s2[j]:
            x = self.helper(s1, i-1, s2, j-1, dp)
            dp[i][j] = x
            return x
        # If not equall, three possible things to do
        else:
            # Edit
            replace = self.helper(s1, i-1, s2, j-1, dp)
            # Replace
            add = self.helper(s1, i, s2, j-1, dp)
            # Delete
            delete = self.helper(s1, i-1, s2, j, dp)
            dp[i][j] = min(replace, add, delete)+1
            return min(replace, add, delete)+1

        