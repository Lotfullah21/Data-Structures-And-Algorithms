class Solution:
    def countOccurrence(self,arr, k):
        c = 0
        for i in range(len(arr)):
            if arr[i]==k:
                c+=1
        return c
    
def main():
    if __name__ =="__main__":
        array = list(map(int, input("Enter a list: ").split()))
        target = int(input("Enter the target element: "))
        solution = Solution()
        result = solution.countOccurrence(array, target)
        print("count of target is", result)
main()