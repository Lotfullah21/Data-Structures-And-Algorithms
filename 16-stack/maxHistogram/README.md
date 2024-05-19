#### Question:

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

<a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank">leetcode</a>

```py
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
```

#### Analysis:

`Time Complexity` is `O(3*N)`, for each element, there is a finite number of possibilities, either replace, do not replace or replace and at max replace N element at last if previous could not.
Because we are using two other function to find the next smaller on the left and on the right, its time complexity is `O(2*N)` + `O(N)` for finding largest histogram.
`Space Complexity` is `O(N)` for stack space

#### Optimized Solution

Here, we do not need ot calculate next smaller on the left and on the right separately, once the smaller element on the right side for current value have been found, the smaller element on the left is the value just bellow the current

```py
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

```

#### Analysis:

`Time Complexity` is `O(N)`, for each element, there is a finite number of possibilities, either replace, do not replace or replace and at max replace N element at last if previous could not.
`Space Complexity` is `O(N)` for stack space
