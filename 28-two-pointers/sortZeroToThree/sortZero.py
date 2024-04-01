class Solution:
    def sort023(self, arr: list) -> list:
        self.arr = arr
        n = len(self.arr)
        i = 0
        j = 0
        k = n-1
        while j<=k:
            if self.arr[j]==0:
                self.swap(i,j)
                i+=1
                j+=1
            elif self.arr[j] == 2:
                self.swap(j, k)
                k-=1
            else:
                j+=1
        return arr

    def swap(self, i, j):
            temp = self.arr[i]
            self.arr[i] = self.arr[j]
            self.arr[j] = temp

arr = [0,1,1,1,0,1,1,2,1,2,2]
solution = Solution()
result = solution.sort023(arr)
print(result)