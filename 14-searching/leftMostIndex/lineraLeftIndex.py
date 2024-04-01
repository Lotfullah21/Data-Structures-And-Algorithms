class Solution:
    ##Complete this function
    def leftIndex(self,arr, K):
        #Your code here
        for i in range(len(arr)):
            if arr[i]==K:
                return i
        return -1
    


def main():
    if __name__ =="__main__":
        array = list(map(int, input("Enter a list: ").split()))
        target = int(input("Enter the target element: "))
        solution = Solution()
        result = solution.leftIndex(array, 3)
        print("the left most index of the target is", result)
main()