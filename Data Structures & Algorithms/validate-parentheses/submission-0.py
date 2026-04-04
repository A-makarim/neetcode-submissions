class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', ']':'[', '}':'{'}   

        stack = []  

        for char in s:
            if char in match.values():
                stack.append(char)

            else:
                if not stack:          
                    return False
                if stack[-1] != match[char]:   
                    return False
                stack.pop()

        return len(stack) == 0
