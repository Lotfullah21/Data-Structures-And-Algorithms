class Solution:
    def rotate(self, nums: list, k: int) -> None:
        n = len(nums)
        k = k % n

        print("Original array:", nums)

        # reverse the whole array
        self.reverse(nums, 0, n - 1)
        print("After reversing whole array:", nums)

        # reverse the first k elements
        self.reverse(nums, 0, k - 1)
        print(f"After reversing first {k} elements:", nums)

        # reverse the remaining elements
        self.reverse(nums, k, n - 1)
        print(f"After reversing remaining {n - k} elements:", nums)

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            # swap the elements
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


def main():
    # Sample input as provided by LeetCode
    nums = [1,2,3,45,6,7,8,9,9,1021]
    k = 2

    solution = Solution()
    solution.rotate(nums, k)

    # Output the result in the format expected by LeetCode
    print("Final result:", nums)


if __name__ == "__main__":
    main()
