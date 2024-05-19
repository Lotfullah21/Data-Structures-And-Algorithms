
class Solution:
    def insert(self, array, n):
        self.insertionSort(self, array, n)
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, array: list, n:int) -> list:
        # For each element, do insertion sort;How?compare the j+1th with jth element.
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if array[j]>array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                else:
                    break
        return array
    
array = [9, 0, -1, 2, 5]
solution = Solution()
result = solution.insertionSort(array,5)
print(result)