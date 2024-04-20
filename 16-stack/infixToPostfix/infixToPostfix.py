class Solution:
    def infixToPostfix(self, expression):
        operands = []
        operators = []
        i = 0
        while i<len(expression):
            ch = expression[i]
            if ch=="(":
                operators.append(ch)
            elif ch==")":
                while operators[-1]!="(":
                    operator = operators.pop()
                    value2 = operands.pop()
                    value1 = operands.pop()
                    calculated = value1+value2+operator
                    operands.append(calculated)
                # Remove the "(" parenthesis
                operators.pop()
            elif ch in {"+","*","-","/","^"}:
                while operators and self.precedence(operators[-1])>=self.precedence(ch):
                    operator = operators.pop()
                    value2 = operands.pop()
                    value1 = operands.pop()
                    calculated = value1+value2+operator
                    operands.append(calculated)
                operators.append(ch)
            # If it is a number character, just add it to the operands stack.
            else:
                operands.append(ch)
            i+=1
        # If still, there are some operators remaining in the operators stack.
        while operators:
            operator = operators.pop()
            value2 = operands.pop()
            value1 = operands.pop()
            calculated = value1+value2+operator
            operands.append(calculated)
        return operands.pop()
        
    def precedence(self, c):
        if c == "^":
            return 4
        elif c in {"*", "/"}:
            return 3
        elif c in {"+", "-"}:
            return 2
        elif c in {"(", ")"}:
            return 1
        else:
            return 0
# Example usage
solution = Solution()
infix_expression = "A+B*C-(D/E^F)"
result = solution.infixToPostfix(infix_expression)
print("Result:", result)