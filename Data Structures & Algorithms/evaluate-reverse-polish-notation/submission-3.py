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
                    b= int(stack.pop())
                    a= int(stack.pop())
                    ans = a//b
                stack.append(ans)
            else: 
                stack.append(i)

        return stack[0]
