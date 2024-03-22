
class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        # code here
        if n<=0:
            return 0
        if n==1:
            return 1
        else:
            return self.sumOfDigits(n//10) + (n%10)