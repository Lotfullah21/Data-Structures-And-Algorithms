
class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        # code here
        if n<10:
            return n
        
        else:
            return self.sumOfDigits(n//10) + (n%10)
        


def main():
    if __name__ == "__main__":
        solution = Solution()
        result = solution.sumOfDigits(234)
        print(result)
    
main()