from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * (n - k + 1)
        dq = deque()
        # For first window
        for i in range(k):
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])

        answer[0] = dq[0]
        # For the remaining window starting from k-1th window, but index wise, start from kth.
        for i in range(k, n):
            if nums[i - k] == dq[0]:
                dq.popleft()
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])
            answer[i - k + 1] = dq[0]

        return answer



def main():
    arr = [1, 3,0,2,8, 9, 12]
    solution = Solution()
    result = solution.maxSlidingWindow(arr, 3)
    print("max sliding window =", result)

if __name__ == "__main__":
    main()