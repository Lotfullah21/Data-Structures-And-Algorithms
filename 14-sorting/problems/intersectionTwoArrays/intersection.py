class Solution:
    def printIntersection(self,arr1, arr2, N, M):
        "Returns the elements that are both present in arr1 and arr2"
        result = []
        i, j = 0, 0
        
        while i < N and j < M:
            # If the current elements are equal and not a duplicate, add to result
            if arr1[i] == arr2[j]:
                # If not result is added to avoid out of index error for result array, because at first iteration it is empty to check for arr[-1].
                # It check if result is empty.
                # if len(result)==0 or  result[-1] != arr1[i]:
                if not result or  result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
            # If arr1[i] is smaller, move to the next element in arr1
            elif arr1[i] < arr2[j]:
                i += 1
            # If arr2[j] is smaller, move to the next element in arr2
            else:
                j += 1
        
        # If no common elements, return [-1]
        if not result:
            return [-1]
        
        return result
    
# Test the function
solution = Solution()
arr1 = [1,2, 3, 4]
arr2 = [2, 4, 6, 7, 8]
N = len(arr1)
M = len(arr2)
result = solution.printIntersection(arr1, arr2, N, M)
print(result)

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6, 7, 8]
N = len(arr1)
M = len(arr2)
result = solution.printIntersection(arr1, arr2, N, M)
print(result)

arr1 = [1, 2]
arr2 = [3, 4]
N = len(arr1)
M = len(arr2)
result = solution.printIntersection(arr1, arr2, N, M)
print(result)