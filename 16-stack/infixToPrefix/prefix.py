class Solution:
    def infixToPrefix(self, expression):
        operators = []
        result = []
        i = len(expression) - 1
        while i >= 0:
            c = expression[i]
            if c == ")":
                operators.append(c)
            elif c == "(":
                while operators and operators[-1] != ")":
                    operator = operators.pop()
                    value1 = result.pop()
                    value2 = result.pop()
                    cal = operator + value1 + value2
                    result.append(cal)
                operators.pop()  
            elif c in {"+","-","*","^","/"}:
                while operators and self.precedence(c) <= self.precedence(operators[-1]):
                    operator = operators.pop()
                    # As we are moving from right to left, the value1 will be the first element that is popped out.
                    value1 = result.pop()  
                    value2 = result.pop()
                    cal = operator + value1 +  value2
                    result.append(cal)
                operators.append(c)
            else:
                result.append(c)
            i -= 1

        while operators:
            operator = operators.pop()
            value1 = result.pop()  
            value2 = result.pop()
            cal = operator + value1 + value2
            result.append(cal)
            
        return result[-1]

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

solution = Solution()
expression = "(A-B/C)*(A/K-L)"
result = solution.infixToPrefix(expression)
print("Prefix:", result)
