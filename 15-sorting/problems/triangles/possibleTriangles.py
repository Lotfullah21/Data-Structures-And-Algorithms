class Solution:
    def findNumberOfTriangles(self, arr: list, n: int) -> int:
        """Calculates and returns number of possible triangles that can be formed from arr

        Args:
            arr (list): list of sides(a,b,c)
            n (int): length of the array

        Returns:
            int: number of possible triangles out of all sides in the arr.
        """
        # Sort the array in non-decreasing order
        arr.sort()
        count = 0
        # Keep the bottom side of the triangle fixed.
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    # If condition satisfies, triangles can be formed
                    count = count + right - left
                    # After doing the whole counting from current left to right, decrement the index of right side.
                    right -= 1
                else:
                    # when arr[left]+arr[right]<arr[c]; increment left
                    left += 1

        return count