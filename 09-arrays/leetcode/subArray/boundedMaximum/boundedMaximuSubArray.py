from typing import List
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], left: int, right: int) -> int:
        # The index after the index value which is greater than left and right
        leastGreatestIndex = 0
        # Keeping the count of the last valid counts we have.
        lastValidCount = 0
        answer = 0
        for ep in range(len(A)):
            if left <= A[ep] <= right:
                # number of sub arrays if number is within range of left and right
                answer = answer +  ep - leastGreatestIndex + 1
                # To keep track of last valid starting points
                lastValidCount = ep - leastGreatestIndex + 1
            elif A[ep] < left:
                # If the value is smaller than left index value, number of sub arrays it can contain within that bound is equal to the previous counts.
                answer = answer +  lastValidCount
            else: # ep > left and ep>right.
                # then nullify the contribution of previous counts and update the leastGreatestIndex to one index after the current end point index.
                leastGreatestIndex = ep + 1
                lastValidCount = 0

        return answer
