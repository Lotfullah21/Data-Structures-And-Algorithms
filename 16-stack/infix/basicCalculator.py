class Solution:
    def calculate(self, s: str) -> int:
        operands = []
        operators = []
        i = 0
        while i<len(s):
            ch = s[i]
            if "0"<=ch<="9":
                num = 0
                # Convert a strings of numbers into an integer.
                while i<len(s) and "0"<=s[i]<="9":
                    num  = num*10+int(s[i])
                    i+=1
                operands.append(num)
                # Because while generating numbers, we moved one step ahead.
                i-=1
                
            elif ch in {"+","/","*","-"}:
                # Once an operator is encountered that is smaller than the operator which is there in stack, calculate all the operations before current operator and add it after finishing all the calculations.
                while operators and self.precedence(operators[-1])>=self.precedence(ch):
                    operator = operators.pop()
                    val2 = operands.pop()
                    val1 = operands.pop()
                    calc = self.calculator(val1,val2,operator)
                    operands.append(calc)
                operators.append(ch)
            i+=1
        # When the whole string is traversed, but still some operators and operands are there in the stack.
        while operators:
            operator = operators.pop()
            val2 = operands.pop()
            val1 = operands.pop()
            calc = self.calculator(val1,val2,operator)
            operands.append(calc)
        return operands[0]
    
    def calculator(self, a: int, b: int, c: str) -> int:
        if c == '+':
            return a + b
        elif c == '-':
            return a - b
        elif c == '*':
            return a * b
        return int(a / b)
    
    def precedence(self, operator: str):
        if operator=="+" or operator=="-":
            return 0
        else:
            return 1
# Example usage
sol = Solution()
expression = "4+2/2"
result = sol.calculate(expression)
print("Result:", result)

        
            
        