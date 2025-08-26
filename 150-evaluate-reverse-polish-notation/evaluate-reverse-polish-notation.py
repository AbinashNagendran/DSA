class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        operators = {"+", "-", "*", "/"}
        for val in tokens: 
            if val in operators:
                num2, num1 = int(stack.pop()), int(stack.pop())
                match val:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = int(num1 / num2)
                stack.append(str(result))
            else:
                stack.append(val)
        return int(stack[0])