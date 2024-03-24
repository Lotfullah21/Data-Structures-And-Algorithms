class Solution:
def majorityElement(self, nums):
val1, count1 = nums[0], 1
val2, count2 = nums[0], 0

        for i in range(1, len(nums)):
            if nums[i] == val1:
                count1 += 1
            elif nums[i] == val2:
                count2 += 1
            elif count1 == 0:
                val1, count1 = nums[i], 1
            elif count2 == 0:
                val2, count2 = nums[i], 1
            else:
                count1 -= 1
                count2 -= 1

        c1, c2 = 0, 0

        for val in nums:
            if val == val1:
                c1 += 1
            elif val == val2:
                c2 += 1

        ans = []
        if c1 > len(nums) // 3:
            ans.append(val1)

        if c2 > len(nums) // 3:
            ans.append(val2)

        return ans
