class Solution:
    def largestRectangleArea(self, height: list) -> int:
        nser = self.nser(height)
        nsel = self.nsel(height)
        print(heights, nser, nsel)
        print(heights[0], nser[0], nsel[0])
        maxHeight = float("-inf")
        n = len(height)
        for i in range(n):
            currentHeight = height[i] 
            # Inside the nsel and nser, we keep the indices to calculate the width, just the indices.
            rightIndexValue = nser[i] - 1 
            leftIndexValue = nsel[i] + 1
            width = rightIndexValue - leftIndexValue + 1
            area = int(currentHeight * width)
            maxHeight = max(maxHeight, area)
        return maxHeight

    def nser(self, height: list) -> list:
        n = len(height)
        stack = []
        nextSmallerIndices = [n] * n
        for i in range(n):
            while len(stack) > 0 and height[i] < height[stack[-1]]:
                idx = stack.pop()
                nextSmallerIndices[idx] = i
            stack.append(i)
        return nextSmallerIndices

    def nsel(self, height: list) -> list:
        n = len(height)
        stack = []
        nextSmallerIndices = [-1] * n
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and height[i] < height[stack[-1]]:
                idx = stack.pop()
                nextSmallerIndices[idx] = i
            stack.append(i)
        return nextSmallerIndices


solution = Solution()
heights = [2, 4, 2, 3, 4, 1, 100]
result = solution.maxHistogram(heights)
print(result)
