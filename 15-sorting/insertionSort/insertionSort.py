
class Solution:
    def insert(self, array, index, n):
        self.insertionSort(self, array, n)
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, array, n):
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if array[j]>array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                else:
                    break
        return array