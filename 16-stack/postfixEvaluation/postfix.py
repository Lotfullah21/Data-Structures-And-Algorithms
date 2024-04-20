class Solution:
    def postfixEvaluation(self,expression: str):
        i = 0
        operands = []
        while i<len(expression):
            ele = expression[i]
            if ele.isalnum():
                operands.append(int(ele))
            elif ele in {"+","-","/","*"}:
                value2 = operands.pop()
                value1 = operands.pop()
                value = self.calculate(value1,value2,ele)
                operands.append(value)
            i+=1
        return operands[-1]
    def calculate(self, a, b, c):
        if c=="+":
            return a+b
        elif c=="-":
            return a-b
        elif c=="/":
            return a/b
        elif c=="*":
            return a*b
        
solution = Solution()
expression = "42+9*"
result = solution.postfixEvaluation(expression)
print("Result:", result)