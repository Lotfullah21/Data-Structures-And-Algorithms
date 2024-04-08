class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        answer = 0
        for i in range(len(heights) + 1):
            # If There are elements that does not have next smaller on right, compare them with zero.
            temp = 0
            if i== len(heights):
                temp = 0
            else:
                temp = heights[i]
            while len(stack)>0 and temp < heights[stack[-1]]:
                toBeSolvedIndex = stack.pop()
                nextSmallerOnRightIndex = i
                x1 = nextSmallerOnRightIndex - 1
                # Take care of the case when there is no smaller elements on left.
                nextSmallerOnLeftIndex = -1
                if len(stack)==0:
                    nextSmallerOnLeftIndex = -1
                else:
                    nextSmallerOnLeftIndex = stack[-1]
                x2 = nextSmallerOnLeftIndex + 1
                area = heights[toBeSolvedIndex] * (x1 - x2 + 1)
                answer = max(answer, area)
            stack.append(i)
        return answer

# Example usage
solution = Solution()
heights = [2, 1, 5, 6, 2, 3]
result = solution.largestRectangleArea(heights)
# Print the result
print(result)
