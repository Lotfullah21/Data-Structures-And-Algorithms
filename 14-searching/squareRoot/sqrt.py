class Solution:
    def squareRoot(self, x):
        low = 0
        high = x
        ans = -1 
        while (low<=high):
            mid = (low+high)//2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt>x:
                high = mid - 1
            else:
                low = mid + 1
                # Keep the lower values as your answer
                ans = mid 
        return ans
        
    
    
def main():
    if __name__ =="__main__":
        target = int(input("Enter the target element: "))
        solution = Solution()
        result = solution.squareRoot(target)
        print("square root of",target,"is", result)
main()