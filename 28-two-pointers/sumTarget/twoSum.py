class Solution:
    class Pair:
        def __init__(self, num, idx):
            self.num = num
            self.idx = idx

        def __lt__(self, other):
                # If two numbers are different
                if self.num!=other.num:
                # The number with lesser value comes before other.value.
                    if self.num<other.num:
                        return True
                # If Two numbers are the same.
                else:
                    # Sort based on which ever comes first.
                    if self.idx<other.idx:
                        return True

    def two_sum(self, nums, target):
        n = len(nums)
        arr = [self.Pair(nums[i], i) for i in range(n)]
        arr.sort()

        i = 0
        j = n - 1

        while i < j:
            left = arr[i].num
            right = arr[j].num
            totalVal = left + right

            if totalVal == target:
                return [arr[i].idx, arr[j].idx]
            elif totalVal < target:
                i += 1
            else:
                j -= 1

        return [0, 0]

# Example usage:
solution = Solution()
nums = [3, 2, 400, 90]
target = 402
result = solution.two_sum(nums, target)
print(result)
