class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        ops = {
            "+": operator.add, 
            "-": operator.sub, 
            "*": operator.mul, 
            "/":operator.truediv
        }
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                second = stack.pop()
                first = stack.pop()
                result = ops[token](int(first), int(second))
                stack.append(result)
        return int(stack[-1])
