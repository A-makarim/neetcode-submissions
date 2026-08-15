class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:
            if i in "+-*/":
                if i == "+":
                    ans = int(stack.pop()) + int(stack.pop())
                if i == "-":
                    ans = -int(stack.pop()) + int(stack.pop())
                if i == "*":
                    ans = int(stack.pop()) * int(stack.pop())
                if i == "/":
                    ans = 1 / int(stack.pop()) // int(stack.pop())
                stack.append(ans)
            else: 
                stack.append(i)

        return stack[0]
