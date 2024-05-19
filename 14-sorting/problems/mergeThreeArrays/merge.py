class Solution:
    def mergeThree(self, arr1, arr2, arr3,arr4):
        "Returns and merges all of the given three arrays."
        i = 0
        j = 0
        k = 0
        r = 0
        result = []
        while i<len(arr1) or j<len(arr2) or k<len(arr3) or r<len(arr4):
            minVal = float("inf")
            if i<len(arr1):
                minVal = min(minVal,arr1[i])
            if j<len(arr2):
                minVal = min(minVal, arr2[j])
            if k<len(arr3):
                minVal = min(minVal, arr3[k])
            if r<len(arr4):
                minVal = min(minVal, arr4[r])
            result.append(minVal)
            if i<len(arr1) and arr1[i]==minVal:
                i+=1
            elif j<len(arr2) and arr2[j]==minVal:
                j+=1
            elif k<len(arr3) and arr3[k]==minVal:
                k+=1
            elif r<len(arr4) and arr4[r]==minVal:
                r+=1
            # print(result)
        return result
                
                

# Test the function
solution = Solution()
A = [1, 2, 3, 4]
B = [1, 2, 3, 4, 5]
C = [1, 2, 3, 4, 5, 6]
D = [5, 6, 7, 8, 9, 1, 1]
result = solution.mergeThree(A, B, C,D)
print(result)

A = [1, 2]
B = [2, 3, 4]
C = [4, 5, 6, 7]
D = [0,0,1,1]
result = solution.mergeThree(A, B, C,D)
print(result)
