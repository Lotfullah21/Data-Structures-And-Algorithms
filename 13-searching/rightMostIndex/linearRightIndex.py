class Solution:
    ##Complete this function
    def rightIndex(self,arr, K):
        #Your code here
        for i in range(len(arr)-1, -1, -1):
            if arr[i]==K:
                return i
        return -1
    


def main():
    if __name__ =="__main__":
        array = list(map(int, input("Enter a list: ").split()))
        target = int(input("Enter the target element: "))
        solution = Solution()
        result = solution.rightIndex(array, target)
        print("the right most index of the target is", result)
main()